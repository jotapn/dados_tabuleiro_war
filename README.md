Este projeto foi feito em Python 3.11

# Motivo da criação:
WAR é um jogo de estratégia para ser jogado por no mínimo 3 
pessoas e no máximo 6. 
A cada jogador cabe um objetivo quesó deve ser conhecido por ele 
mesmo, e para alcancar tal objetivo, é necessário
realizar ataques aos seus adversários. 
Dificilmente um jogador conseguirá ganhar confiando apenas na sorte: uma boa dose de 
estratégia é fundamental para quem quiser ser vencedor.

Os ataques no jogos constistem em uma disputa de até 3 dados entre ataque e defesa,
 no qual com um tempo de jogo, as batalhas entre adversários diversas vezes se obtém várias tropas, sendo necessário arremessar
os dados diversas vezes, deixando a jogatina por muitas vezes cansativa.

Para amenizar esse repetitividade no jogo, foi feito esse script que agiliza o processo de batalha,
principalmente as que envolvem muitas tropas.

# Como funciona o programa:
Primeiramente é solicitado a quantidade de tropas do ataque e posteriormente as da defesa, com isso
é realizada a confirmação do ataque. Após os dados serem "jogados" o programa devolve os valores dos dados de ataque
e os da defesa, além de mostrar quantas tropas restaram de cada jogador.

### Iniciando
As bibliotecas utilizadas foram: Random, time e os. 
Logo, não é necessário realizar a instalação de outra biblioteca externa.

Para inicializar o programa, basta executar o arquivo "menu.py", nele é possível iniciar o jogo e/ou verificar as regras 
de ataque e batalha do WAR.