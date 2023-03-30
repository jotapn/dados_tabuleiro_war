import os
import random
from time import sleep


class War:
    def __init__(self):
        self.tropas_perdidas_defesa = 0
        self.tropas_perdidas_ataque = 0
        self.tropa_defesa = None
        self.tropa_ataque = None

    def limpar_tela(self):
        os.system('cls')

    def jogar(self):
        self.apresentacao()

        self.pede_tropa()

        continuar = False

        if not self.valida_ataque() or not self.confirmando_ataque():
            return continuar == True

        while not continuar:
            self.limpar_tela()
            if not self.valida_ataque():
                break

            self.dados_ataque = self.rolar_dados_ataque()
            self.dados_defesa = self.rolar_dados_defesa()

            print(f'Dados do ataque: {self.dados_ataque}')
            print(f'Dados da defesa: {self.dados_defesa}')

            self.calcular_ataque()

            self.apresentar_novas_tropas()

            continuar = True if self.continuar_ataque() else False

            if self.tropa_defesa == 0:
                print('As tropas de Defesa foram derrotadas!')
                break

    def apresentacao(self):
        self.limpar_tela()
        print('********************')
        print('* INICIO DO ATAQUE *')
        print('********************')

    def pede_tropa(self):
        self.tropa_ataque = int(input('Indique quantidade de tropas de ATAQUE:'))
        self.tropa_defesa = int(input('Indique quantidade de tropas de DEFESA:'))

    def valida_ataque(self):
        if self.tropa_ataque < 2:
            print('Você não pode atacar, pois possui apenas 1 exército, Ataque encerrado!\n')
            return False
        elif self.tropa_defesa < 1:
            print('É necessário pelo menos um exército de defesa!, refaça seu ataque!\n')
            return False
        else:
            return True

    def confirmando_ataque(self):
        self.limpar_tela()
        confirma = int(input(
            f'Você irá atacar com {self.tropa_ataque} exércitos contra {self.tropa_defesa} tropas de defesas.\n'
            f'Tem certeza disso?\n'
            f'[0] Sim - [1] Cancelar ataque - [2] Refazer ataque\n'
        ))
        if confirma == 0:
            print('Atacando...')
            sleep(1)
            return True
        elif confirma == 1:
            print('O ataque foi cancelado!')
            return False
        elif confirma == 2:
            self.reiniciar_jogada()
        else:
            raise Exception('Opção inválida!')

    def reiniciar_jogada(self):
        self.limpar_tela()
        print('Iniciando novo ataque...')
        sleep(1)
        self.tropa_defesa = None
        self.tropa_ataque = None
        self.jogar()

    def rolar_dados_ataque(self):
        if self.tropa_ataque > 3:  # ataca com 3 dados
            return self._dado(3)
        elif self.tropa_ataque == 3:  # ataca com 2 dados
            return self._dado(2)
        elif self.tropa_ataque == 2:  # ataca com 1 dado
            return self._dado(1)

    def rolar_dados_defesa(self):
        if self.tropa_defesa >= 3:  # defende com 3 dados
            return self._dado(3)
        elif self.tropa_defesa == 2:  # defende com 2 dados
            return self._dado(2)
        elif self.tropa_defesa == 1:  # defende com 1 dado
            return self._dado(1)

    @staticmethod
    def _dado(jogar_x_vezes):
        lista_de_dados = []
        for i in range(0, jogar_x_vezes):
            jogar_dado = random.randint(1, 6)
            lista_de_dados.append(jogar_dado)
        lista_de_dados.sort()
        return lista_de_dados

    def perda_de_pontos(self):
        self.tropas_perdidas_defesa = 0
        self.tropas_perdidas_ataque = 0

        for i in range(self.tamanho_ataque):
            if self.dados_defesa[i] >= self.dados_ataque[i]:
                self.tropas_perdidas_ataque += 1
            else:
                self.tropas_perdidas_defesa += 1

    def calcular_ataque(self):
        self.tamanho_ataque = len(self.dados_ataque)
        tamanho_defesa = len(self.dados_defesa)

        if self.tamanho_ataque == tamanho_defesa:
            self.perda_de_pontos()

        elif self.tamanho_ataque - tamanho_defesa == 1:
            self.dados_ataque.pop(0)
            self.tamanho_ataque = len(self.dados_ataque)
            self.perda_de_pontos()

        elif self.tamanho_ataque - tamanho_defesa == -1:
            self.dados_defesa.pop(0)
            self.tamanho_ataque = len(self.dados_ataque)
            self.perda_de_pontos()

        elif self.tamanho_ataque - tamanho_defesa == 2:
            self.dados_ataque.pop(0)
            self.dados_ataque.pop(0)
            self.tamanho_ataque = len(self.dados_ataque)
            self.perda_de_pontos()

        else:
            self.dados_defesa.pop(0)
            self.dados_defesa.pop(0)
            self.tamanho_ataque = len(self.dados_ataque)
            self.perda_de_pontos()

        self.tropa_ataque -= self.tropas_perdidas_ataque
        self.tropa_defesa -= self.tropas_perdidas_defesa
        return [self.tropa_ataque, self.tropa_defesa]

    def apresentar_novas_tropas(self):
        print(f'\nTropas de ataque restantes: {self.tropa_ataque}')
        print(f'Tropas de defesa restantes: {self.tropa_defesa}\n')

    def perguntar_ataque(self):
        pergunta = int(input(f'\nVocê deseja continuar atacando?\n[0] SIM - [1] NÃO\n'))
        if pergunta == 0:
            print('Atacando...')
            sleep(0.2)
            return False
        elif pergunta == 1:
            print('O ataque foi encerrado!')
            return True

    def continuar_ataque(self):
        if self.tropa_defesa !=0:
            return self.perguntar_ataque()
        else:
            print('ATAQUE ENCERRADO!')
            print('DEFESAS DERROTADAS!')
            sleep(0.5)
            pergunta = int(input(f'\nVocê deseja fazer NOVO ataque?'
                                 f'\n[0] SIM - [1] NÃO\n'))
            if pergunta == 0:
                self.reiniciar_jogada()
            elif pergunta == 1:
                print('O ataque foi encerrado!')
                return True

class Regras:
    def regra_para_atacar(self):
        regra_ataque = (
                 f'REGRAS PARA O ATAQUE:\n'
                 f'01) O atacante usa os dados vermelhos e o jogador de defesa usa os dados amarelos.\n'
                 f'\n02) O ataque, a partir de um território qualquer conquistado, só pode ser dirigido a um território\n'
                 f'adversário com fronteiras em comum (território contiguo) ou ligado através de um pontilhado\n'
                 f'(como a Terra é redonda, pode-se atacar Vladivostok a partir do Alaska, e vice-versa).\n'
                 f'\n03) O atacante deve anunciar de que território vai partir o ataque e qual o território atacado,\n'
                 f'bem como deve anunciar com quantos exércitos estará atacando.\n'
                 f'\n04) Para que um ataque possa partir de um território, ele deve ter pelo menos 2 exércitos\n'
                 f'(um exército de ocupação e um para efetuar o ataque).\n'
                 f'\n05)Cada ataque pode ser feito com um, dois ou três exércitos. Portanto, o número máximo de exércitos\n'
                 f'participantes em cada ataque é três, mesmo que haja mais exércitos no território atacante.\n'
                 f'\n06)Ataca-se um território independentemente do seu número de exércitos.\n'
                 f'\n07) O território de defesa pode usar, inclusive, o exército de ocupação para se defender.\n'
                 f'\n08) Na sua vez de jogar, cada participante pode atacar tantas vezes quantas quiser para conquistar um\n'
                 f'território adversário.\n'
                 f'\n09) Os ataques podem partir de um ou vários territórios, mas sempre um de cada vez, de acordo com\n'
                 f'estratégia do atacante. O jogador também pode atacar vários territórios.\n'
                 f'\n10) A cada ataque deve haver nova confrontação de dados (ver explicação adiante).\n'
                 f'\n11) O jogador atacante jogará com tantos dados quantos forem os seus exércitos participantes da\n'
                 f'batalha, ocorrendo o mesmo com o jogador da defesa. Assim, se o atacante usar 3 exércitos\n'
                 f'contra I da defesa, ele jogará 3 dados contra I do defensor.\n')
        print(regra_ataque)

    def regra_de_batalha(self):
        regra_batalha = (
            f'\nREGRA DA BATALHA:\n'
            f'  No caso do atacante possuir 4 exércitos em seu território e o defensor possuir 3,\n'
                f'ambos podem jogar com 3 dados, ou seja, tanto o atacante (Congo) quanto o defensor (África do Sul)\n'
                f'lutam com três exércitos. Após a batalha (realizada através do lançamento dos dados), é feita a\n'
                f'comparação dos pontos do atacante com os pontos do defensor, para se decidir quem ganha e quem perde\n'
                f'exércitos. Compara-se o maior ponto do dado atacante com o maior ponto do dado defensor.\n'
                f'A vitória será de quem tiver o ponto maior. No caso de empate, a vitória será da defesa\n'
            f'\n  Em seguida, compara-se o segundo maior ponto do atacante com o segundo maior do defensor:\n'
                f'a vitória será decidida como no caso anterior. Por fim, são comparados os menores valores, com base\n'
                f'no mesmo procedimento.\n'
            f'\n  Supondo-se que o atacante tenha tirado 5, 4 e 1 e o defensor 6, 3 e 1, a comparação será feita da\n'
                f'seguinte forma:\n'
                f'\nCOMPARAÇÃO    |  ATAQUE  |  DEFESA  |  VENCEDOR  |   RESULTADO   |\n'
                f'MAIOR         |     5    |    6     |   DEFESA   | ATAQUE PERDE 1|\n'
                f'SEGUNDO MAIOR |     4    |    3     |   ATAQUE   | DEFESA PERDE 1|\n'
                f'MENOR         |     1    |    1     |   DEFESA   | ATAQUE PERDE 1|\n'
                )
        print(regra_batalha)