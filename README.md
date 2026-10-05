# Jogo da Forca em Python

Projeto desenvolvido em Python com o objetivo inicial de praticar e aprimorar minha lógica de programação.

O jogo funciona de maneira semelhante ao jogo da forca tradicional: o jogador deve descobrir uma palavra digitando uma letra por vez. A cada tentativa incorreta, uma parte do corpo do boneco é adicionada à forca. Caso o corpo seja completado antes que a palavra seja descoberta, o jogador perde a partida.


## 🎮 Funcionamento

Ao iniciar o jogo, o jogador deve escolher entre os idiomas disponíveis:

- Português (Brasil)
- English

Após escolher o idioma, todas as mensagens exibidas durante a partida são apresentadas na linguagem selecionada.

Durante a partida:

1. O jogador recebe uma palavra secreta.
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

- Sistema completo de jogo da forca
- Validação de uma letra por tentativa
- Validação de caracteres inválidos
- Impedimento de letras repetidas
- Suporte a palavras com acentos
- Normalização de acentos para comparação das letras
- Sistema de vitória e derrota
- Contagem de tentativas
- Exibição das partes do corpo adicionadas à forca
- Opção de continuar ou encerrar a partida
- Suporte a múltiplos idiomas
- Português (Brasil)
- Inglês



## 🧠 Desenvolvimento

Inicialmente, o projeto foi criado como uma forma de praticar lógica de programação e desenvolver minha familiaridade com Python.

Durante o desenvolvimento, o código passou por algumas mudanças estruturais. Uma das principais foi a divisão do programa em funções, tornando o código mais organizado e facilitando futuras alterações e implementações.

Outro desafio foi implementar o suporte a palavras com acentos. O programa utiliza normalização de caracteres para permitir que letras sejam comparadas corretamente mesmo quando possuem acentos.

Por exemplo, em uma palavra como:

`coração`

o jogador pode utilizar `a` para encontrar a letra `ã`.

Também foi implementado um sistema de múltiplos idiomas, permitindo que o jogador escolha a linguagem antes de iniciar a partida. A linguagem escolhida é utilizada durante todo o jogo.



## 🚀 Próximas atualizações

O projeto ainda está em desenvolvimento e possui algumas funcionalidades planejadas.

### Banco de dados

A próxima etapa será implementar um banco de dados para armazenar as palavras utilizadas pelo jogo.

A intenção é fazer com que cada nova partida possa receber uma palavra armazenada no banco de dados, evitando depender de uma lista fixa diretamente no código.

Também pretendo organizar as palavras de acordo com o idioma escolhido pelo jogador.



## 🛠️ Tecnologias utilizadas

- Python
- Git
- GitHub

### Bibliotecas utilizadas

- `random`
- `os`
- `unicodedata`