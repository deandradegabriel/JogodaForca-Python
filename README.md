# Jogo da Forca em Python

Projeto desenvolvido em Python com o objetivo de praticar lógica de programação, aprimorar conhecimentos na linguagem e aplicar conceitos de organização de código, manipulação de dados e integração com banco de dados.

O jogo funciona de maneira semelhante ao tradicional jogo da forca, no qual o jogador deve descobrir uma palavra secreta digitando uma letra por vez. A cada tentativa incorreta, uma parte do corpo é adicionada à forca. Caso o corpo seja completado antes que a palavra seja descoberta, o jogador perde a partida.

## 🎮 Funcionamento

Ao iniciar o programa, o jogador deve selecionar um dos idiomas disponíveis:

- Português (Brasil)
- English

Após a seleção, todas as mensagens apresentadas durante a partida são exibidas no idioma escolhido.

Durante o jogo:

1. O jogador recebe uma palavra secreta selecionada aleatoriamente do banco de dados.

2. Uma letra deve ser informada por tentativa.

3. O sistema verifica se a letra pertence à palavra.

4. Letras corretas são reveladas na palavra.

5. A cada tentativa incorreta, uma parte do corpo é adicionada à forca.

6. Letras repetidas não são permitidas.

7. O jogador vence quando descobre toda a palavra.

8. O jogador perde quando todas as partes do corpo são adicionadas à forca.

9. Ao final da partida, o jogador pode escolher continuar ou sair.


## ✨ Funcionalidades

Atualmente, o projeto possui:

- Sistema completo de jogo da forca.
- Seleção de idioma antes do início da partida.
- Suporte aos idiomas Português (Brasil) e Inglês.
- Validação de uma letra por tentativa.
- Validação de caracteres inválidos.
- Impedimento de letras repetidas.
- Suporte a palavras com acentos.
- Normalização de caracteres para comparação de letras acentuadas.
- Sistema de vitória e derrota.
- Contagem de tentativas realizadas.
- Exibição das partes do corpo adicionadas à forca.
- Opção de continuar ou encerrar a partida.
- Integração com banco de dados SQLite.
- Seleção aleatória de palavras armazenadas no banco de dados.
- Organização das palavras de acordo com o idioma selecionado.


## 🗄️ Banco de Dados

O projeto utiliza SQLite para armazenar e gerenciar as palavras utilizadas durante as partidas.

A estrutura do banco de dados conta com uma tabela chamada palavras, composta pelas seguintes colunas:

Coluna  | Descrição
:------ | :------
id      | identificador único de palavra.
palavra | palavra armazenada.
idioma  | idioma ao qual a palavra pertence.


O sistema identifica o idioma selecionado pelo jogador e realiza uma consulta ao banco de dados para selecionar aleatoriamente uma palavra correspondente.

Além disso, a inicialização do programa verifica se já existem palavras cadastradas para cada idioma. Caso contrário, os dados iniciais são inseridos automaticamente.

Dessa maneira, o projeto deixa de depender exclusivamente de listas de palavras diretamente no código, permitindo uma organização mais adequada dos dados e facilitando futuras expansões.


## 🧠 Desenvolvimento e Aprendizados

Inicialmente, o projeto foi criado como uma forma de praticar lógica de programação e desenvolver familiaridade com Python.

Durante o desenvolvimento, o código passou por diversas melhorias estruturais e funcionais.

Entre os principais conceitos aplicados, destacam-se:

**Organização e modularização**: divisão do programa em funções, tornando o código mais organizado, reutilizável e fácil de manter.

**Manipulação de strings**: utilização de métodos para validação e tratamento das entradas fornecidas pelo jogador.

**Normalização de caracteres**: utilização da biblioteca unicodedata para permitir a comparação de letras com e sem acentos. Por exemplo, em uma palavra como coração, o jogador pode utilizar a para encontrar a letra ã.

**Estruturas de dados**: utilização de listas e dicionários para armazenar informações, controlar as letras utilizadas e organizar as mensagens nos diferentes idiomas.

**Internacionalização**: implementação de um sistema que permite selecionar o idioma antes do início da partida.

**Banco de dados**: utilização de SQLite para criar tabelas, inserir informações e realizar consultas SQL, permitindo selecionar palavras aleatoriamente de acordo com o idioma escolhido.

Essas implementações contribuíram para ampliar meus conhecimentos em Python e proporcionar contato prático com conceitos importantes do desenvolvimento de software.


## 🚀 Próximas Atualizações

O projeto continua em desenvolvimento e poderá receber novas funcionalidades e melhorias estruturais.


## 🛠️ Tecnologias Utilizadas

### Linguagem
- Python

### Banco de Dados
- SQLite

### Ferramentas
- Git
- GitHub

### Bibliotecas utilizadas

- `os`
- `unicodedata`
- `sqlite3`


## 👨‍💻 Autor

Desenvolvido como projeto de estudo e prática em Python, com foco no aprimoramento contínuo de conhecimentos em programação e desenvolvimento de software.