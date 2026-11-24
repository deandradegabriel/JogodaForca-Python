import unittest
import sqlite3
import tempfile

from pathlib import Path
from io import StringIO
from unittest.mock import patch
from src import jogo_da_forca
from src.jogo_da_forca import (
    Normalizar_Acentos,
    Montar_Palavra_Atual,
    Letra_Repetida,
    Venceu,
    Buscar_Palavra_em_DB,
    Perdeu,
    mensagens,
    Ler_Letra,
    Continuar_Ou_Parar_Jogo,
    Jogar
)
# === Unit Tests ===

class TestNormalizarAcentos(unittest.TestCase):

    def test_remover_acentos(self):
        self.assertEqual(Normalizar_Acentos('coração'), 'coracao')
        self.assertEqual(Normalizar_Acentos('árvore'), 'arvore')
        self.assertEqual(Normalizar_Acentos('programação'), 'programacao')

    def test_palavra_sem_acentos(self):
        self.assertEqual(Normalizar_Acentos('python'), 'python')

class TestLetraRepetida(unittest.TestCase):

    def test_letra_fora_da_lista(self):
        self.assertFalse(Letra_Repetida('a', ['b', 'c']))
    
    def test_letra_na_lista(self):
        self.assertTrue(Letra_Repetida('a', ['a', 'b']))
    
    def test_lista_vazia(self):
        self.assertFalse(Letra_Repetida('a', []))
    
    def test_letra_com_acento(self):
        self.assertTrue(Letra_Repetida('a', ['á']))

class TestMontarPalavraAtual(unittest.TestCase):

    def test_nenhuma_letra_descoberta(self):
        self.assertEqual(Montar_Palavra_Atual('python', []), '______')

    def test_todas_as_letras_descobertas(self):
        self.assertEqual(Montar_Palavra_Atual('python', ['p', 'y', 't', 'h', 'o', 'n']), 'python')
    
    def test_algumas_letras_descobertas(self):
        self.assertEqual(Montar_Palavra_Atual('python', ['p', 't', 'o']), 'p_t_o_')
    
    def test_letras_com_acentos_equivalentes(self):
        self.assertEqual(Montar_Palavra_Atual('coração', ['a']), '___a_ã_')

    def test_palavra_secreta_vazia(self):
        self.assertEqual(Montar_Palavra_Atual('', ['p', 'y', 't', 'h', 'o', 'n']), '')

class TestVenceu(unittest.TestCase):

    def test_palavras_iguais(self):
        self.assertTrue(Venceu('python', 'python'))

    def test_palavra_atual_incompleta(self):
        self.assertFalse(Venceu('pyth_n', 'python'))

    def test_strings_vazias(self):
        self.assertTrue(Venceu('', ''))

    def test_palavras_com_comprimentos_diferentes(self):
        self.assertFalse(Venceu('pytho', 'python'))

    def test_palavras_diferentes(self):
        self.assertFalse(Venceu('coração', 'python'))

class TestBuscarPalavraEmDB(unittest.TestCase):

    def setUp(self):
        self.diretorio_temporario = tempfile.TemporaryDirectory()
        self.addCleanup(self.diretorio_temporario.cleanup)

        self.caminho_banco = Path(self.diretorio_temporario.name) / 'teste.db'

        new_path = patch.object(
            jogo_da_forca,
            'CAMINHO_BANCO',
            self.caminho_banco
        )

        new_path.start()
        self.addCleanup(new_path.stop)

        conexao  = sqlite3.connect(self.caminho_banco)
        cursor = conexao.cursor()

        comando_sql = ('''
            CREATE TABLE IF NOT EXISTS palavras(
            palavra TEXT NOT NULL,
            idioma TEXT NOT NULL
            )
        ''')
        cursor.execute(comando_sql, )

        comando_sql = ('''
            INSERT INTO palavras (palavra, idioma) 
            VALUES (?, ?)
        ''')
        dados = [
            ('computador', 'pt'),
            ('programação', 'pt'),
            ('computer', 'en'),
            ('programming', 'en')
        ]
        
        cursor.executemany(comando_sql, dados)
        conexao.commit()
        conexao.close()
        
    def test_palavra_pt_ser_uma_string(self):
        self.assertIsInstance(Buscar_Palavra_em_DB('pt'), str)
    
    def test_palavra_en_ser_uma_string(self):
        self.assertIsInstance(Buscar_Palavra_em_DB('en'), str)
    
    def test_idioma_invalido(self):
        self.assertIsNone(Buscar_Palavra_em_DB('es'))
    
    def test_idioma_sem_palavras(self):
        conexao  = sqlite3.connect(self.caminho_banco)
        cursor = conexao.cursor()

        comando_sql = ('''
        DELETE FROM palavras 
        WHERE idioma = ?
        ''')

        cursor.execute(comando_sql, ('pt',))

        conexao.commit()
        conexao.close()

        self.assertIsNone(Buscar_Palavra_em_DB('pt'))

    def test_palavra_retornada_existe_no_banco(self):

        chamando_palavra = Buscar_Palavra_em_DB('pt')
        palavras_em_DB = ['computador', 'programação']
        
        self.assertIn(chamando_palavra, palavras_em_DB)

class TestPerdeu(unittest.TestCase):

    def test_jogador_ainda_pode_jogar(self):
        ERROS = 2
        MAX_ERROS = 4
        
        self.assertFalse(Perdeu(ERROS, MAX_ERROS, 'python', 'pt')) 
    
    def test_jogador_perdeu(self):
        ERROS = 4
        MAX_ERROS = 4

        self.assertTrue(Perdeu(ERROS, MAX_ERROS, 'python', 'pt'))

    def test_jogador_ultrapassou_limite(self):
        ERROS = 8
        MAX_ERROS = 4

        self.assertTrue(Perdeu(ERROS, MAX_ERROS, 'python', 'pt'))


    def test_mensagem_de_derrota_pt(self):
        ERROS = 4
        MAX_ERROS = 4

        with patch('sys.stdout', new=StringIO()) as saida:
            Perdeu(ERROS, MAX_ERROS, 'computador', 'pt')

            resultado = saida.getvalue()

        self.assertIn('computador', resultado)
        self.assertIn(
            'Número de erros excedidos, o corpo na forca foi completado!\nVOCÊ PERDEU!!!',
            resultado
            )
        self.assertIn(
            'A palavra secreta era: ',
            resultado
            )

    def test_mensagem_de_derrota_en(self):
        ERROS = 4
        MAX_ERROS = 4

        with patch('sys.stdout', new=StringIO()) as saida:
            Perdeu(ERROS, MAX_ERROS, 'computer', 'en')

            resultado = saida.getvalue()

        self.assertIn('computer', resultado)
        self.assertIn(
            'Maximum number of errors exceeded,the gallows figure is complete!\nYOU LOST!!!',
            resultado
            )
        self.assertIn(
            'The secret word was: ',
            resultado
            )

class TestLerLetra(unittest.TestCase):

    def test_letra_minuscula(self):
        with patch('builtins.input', return_value='a'):
            resultado = Ler_Letra('pt')

        self.assertEqual(resultado, 'a')

    def test_letra_maiuscula(self):
        with patch('builtins.input', return_value='A'):
            resultado = Ler_Letra('pt')

        self.assertEqual(resultado, 'a')
 

    def test_entrada_com_varios_caracteres(self):
        with patch('builtins.input', side_effect=['python', 'a']):
            resultado = Ler_Letra('pt')

        self.assertEqual(resultado, 'a')

    def test_entrada_com_numero(self):
        with patch('builtins.input', side_effect=['2', 'a']):
            resultado = Ler_Letra('pt')

        self.assertEqual(resultado, 'a')

    def test_entrada_com_caractere_especial(self):
        with patch('builtins.input', side_effect=['#', 'a']):
            resultado = Ler_Letra('pt')

        self.assertEqual(resultado, 'a')

    def test_entrada_vazia(self):
        with patch('builtins.input', side_effect=['', 'a']):
            resultado = Ler_Letra('pt')

        self.assertEqual(resultado, 'a')

    def test_entrada_letras_acentuadas(self):
        with patch('builtins.input', return_value='Á'):
            resultado = Ler_Letra('pt')

        self.assertEqual(resultado, 'á')

class TestContinuarOuPararJogo(unittest.TestCase):

    def test_encerrar_jogo_pt(self):
        with patch('builtins.input', side_effect=['não', 'nao']):
            resultado1 = Continuar_Ou_Parar_Jogo('pt')
            resultado2 = Continuar_Ou_Parar_Jogo('pt')

        self.assertFalse(resultado1)
        self.assertFalse(resultado2)

    def test_continuar_jogo_pt(self):
        with patch('builtins.input', return_value='sim'):
            with patch('src.jogo_da_forca.os.system') as limpar_terminal:
                resultado = Continuar_Ou_Parar_Jogo('pt')

        self.assertTrue(resultado)
        limpar_terminal.assert_called_once()

    def test_opcao_invalida_pt(self):
        with patch('builtins.input', side_effect=['teste', 'sim']):
            with patch('sys.stdout', new=StringIO()) as saida:
                resultado = Continuar_Ou_Parar_Jogo('pt')
                mensagem_saida = saida.getvalue()

        self.assertIn(
        'Resposta inválida!!! Tente novamente!!!',
        mensagem_saida
        )
        self.assertTrue(resultado)

        with patch('builtins.input', side_effect=['teste', 'não']):
            resultado = Continuar_Ou_Parar_Jogo('pt')

        self.assertFalse(resultado)

        with patch('builtins.input', side_effect=['teste', 'nao']):
            resultado = Continuar_Ou_Parar_Jogo('pt')

        self.assertFalse(resultado)

    def test_opcoes_maiusculas_pt(self):
        with patch('builtins.input', side_effect=['SIM', 'NÃO', 'NAO']):
            resultado1 = Continuar_Ou_Parar_Jogo('pt')
            resultado2 = Continuar_Ou_Parar_Jogo('pt')
            resultado3 = Continuar_Ou_Parar_Jogo('pt')


        self.assertTrue(resultado1)
        self.assertFalse(resultado2)
        self.assertFalse(resultado3)

    def test_encerrar_jogo_en(self):
        with patch('builtins.input', side_effect=['no', 'n']):
            resultado1 = Continuar_Ou_Parar_Jogo('en')
            resultado2 = Continuar_Ou_Parar_Jogo('en')
        
        self.assertFalse(resultado1)
        self.assertFalse(resultado2)
        
    def test_continuar_jogo_en(self):
        with patch('builtins.input', return_value='yes'):
            with patch('src.jogo_da_forca.os.system') as limpar_terminal:
                resultado = Continuar_Ou_Parar_Jogo('en')

        self.assertTrue(resultado)
        limpar_terminal.assert_called_once()

    def test_opcao_invalida_en(self):
        with patch('builtins.input', side_effect=['test', 'yes']):
            with patch('sys.stdout', new=StringIO()) as saida:
                resultado = Continuar_Ou_Parar_Jogo('en')
                mensagem_saida = saida.getvalue()

        self.assertIn(
        'Invalid Answer!!! Try Again!!!',
        mensagem_saida
        )
        self.assertTrue(resultado)

        with patch('builtins.input', side_effect=['test', 'no']):
            resultado = Continuar_Ou_Parar_Jogo('en')

        self.assertFalse(resultado)

        with patch('builtins.input', side_effect=['test', 'n']):
            resultado = Continuar_Ou_Parar_Jogo('en')

        self.assertFalse(resultado)

    def test_opcoes_maiusculas_en(self):
        with patch('builtins.input', side_effect=['YES', 'NO', 'N']):
            resultado1 = Continuar_Ou_Parar_Jogo('en')
            resultado2 = Continuar_Ou_Parar_Jogo('en')
            resultado3 = Continuar_Ou_Parar_Jogo('en')


        self.assertTrue(resultado1)
        self.assertFalse(resultado2)
        self.assertFalse(resultado3)

# === Integration tests ===

class TestIntegracaoJogo(unittest.TestCase):
    def test_jogador_vence_partida(self):
        with patch('src.jogo_da_forca.Buscar_Palavra_em_DB', return_value='python') as buscar_palavra:

            with patch('sys.stdout', new=StringIO()) as saida:

                with patch('builtins.input', side_effect=['p','y','t','h','o','n']):
                
                    Jogar('pt')
                    mensagem_saida = saida.getvalue()

        self.assertIn(
            '\nPARABÉNS!!! VOCÊ GANHOU!!!',
            mensagem_saida
        )

        buscar_palavra.assert_called_once_with('pt')

    def test_jogador_perde_partida(self):
        with patch('src.jogo_da_forca.Buscar_Palavra_em_DB', return_value='python') as buscar_palavra:

            with patch('sys.stdout', new=StringIO()) as saida:

                with patch('builtins.input', side_effect=['a','b','c','d']):
                
                    Jogar('pt')
                    mensagem_saida = saida.getvalue()

        self.assertIn(
            'VOCÊ PERDEU!!!',
            mensagem_saida
        )

        self.assertIn(
            'A palavra secreta era: python',
            mensagem_saida
        )

        buscar_palavra.assert_called_once_with('pt')


    def test_jogador_repete_letra(self):
        
        with patch('src.jogo_da_forca.Buscar_Palavra_em_DB', return_value='python') as buscar_palavra:

            with patch('sys.stdout', new=StringIO()) as saida:

                with patch('builtins.input', side_effect=['p','p','y','t','h','o','n']) as tentativas:
                
                    Jogar('pt')
                    mensagem_saida = saida.getvalue()

        tentativas.assert_called()
        self.assertEqual(tentativas.call_count, 7)

        self.assertIn('Tentativas: 6', mensagem_saida)

        self.assertIn(
            ' 3. Não são aceitas letras repetidas.',
            mensagem_saida
        )

        self.assertIn(
            '\nPARABÉNS!!! VOCÊ GANHOU!!!',
            mensagem_saida
        )

        buscar_palavra.assert_called_once_with('pt')


if __name__ == '__main__':
    unittest.main()
