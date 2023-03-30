from dados_war import War, Regras
import os


def menu():
    limpar_tela()
    print('Bem vindo ao Dados do War')
    chave = 0
    while chave != 1:
        chave = int(input("Precione [1] para iniciar, [2] para ver as regras:\n"))
        if chave == 1:
            jogar = War()
            jogar.jogar()
        if chave == 2:
            limpar_tela()
            regra = Regras()
            tipo_regra = int(input("Precione [1] para regras de ataque, [2] para ver as regras de batalha:\n"))
            if tipo_regra == 1:
                limpar_tela()
                regra.regra_para_atacar()
            elif tipo_regra == 2:
                limpar_tela()
                regra.regra_de_batalha()

def limpar_tela():
    os.system('cls')

if (__name__ == "__main__"):
    menu()
