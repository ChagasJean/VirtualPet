#                    AUTHOR
# ================================================
#      .-./`)        _______         ,---.    ,---.
#      \ '_ .')     /   __  \        |    \  /    |
#     (_ (_) _)    | ,_/  \__)       |  ,  \/  ,  |
#       / .  \   ,-./  )             |  |\_   /|  |
#  ___  |-'`|    \  '_ '`)           |  _( )_/ |  |
# |   | |   '_ _  > (_)  )  __  _ _  | (_ o _) |  |
# |   `-'  /( ` )(  .  .-'_/  )( ` ) |  (_,_)  |  |
#  \      /(_{;}_)`-'`-'     /(_{;}_)|  |      |  |
#   `-..-'  (_,_)   `._____.'  (_,_) '--'      '--'
# =================================================

import random
import pandas as pd
import win32com.client as win32
import tkinter as tk
from tkinter import messagebox

# CRIAÇÃO DE CLASS PARA O PROGRAMA RODAR


class VirtualPet:

    # AQUI É DEFINIDO OS STATUS INICIAIS DO PET E A DEFINIÇÃO DE NOME
    def __init__(self, nome):
        self.nome = nome
        self.fome = 30
        self.higiene = 30
        self.felicidade = 30
        self.saude_fisica = 30
        self.saude_mental = 30
        self.vivo = True

    # CRIADO O METODO ALIMENTAR E VERIFICAÇÃO DOS LIMITES
    def alimentar(self):
        self.fome += 5
        self.higiene -= 5
        self.felicidade += 5
        self.saude_fisica -= 10
        self.saude_mental += 5
        self.verificar_limites()

    # CRIADO O METODO DE BANHO E VERIFICAÇÃO DE LIMITES
    def banhar(self):
        self.higiene += 5
        self.fome -= 5
        self.felicidade += 5
        self.saude_fisica += 10
        self.saude_mental += 5
        self.verificar_limites()

    # CRIADO O METODO BRINCAR E VERIFICAÇÃO DE LIMITES
    def brincar(self):
        self.felicidade += 5
        self.fome -= 5
        self.higiene -= 5
        self.saude_mental += 5
        self.verificar_limites()

    # CRIADO O METODO DE FUMAR UM CIGARRO E VERIFICAÇÃO DE LIMITES
    def fumar_um(self):
        self.felicidade += 5
        self.fome -= 5
        self.higiene -= 5
        self.saude_fisica -= 10
        self.saude_mental += 10
        self.verificar_limites()

    # AQUI É CRIADO A DEFINIÇÃO DE LIMITES PARA QUE OS NÚMEROS NÃO PASSEM DOS VALORES ESTIPULADOS
    def verificar_limites(self):

        if self.fome < 0:
            self.fome = 0
        elif self.fome > 100:
            self.fome = 100

        if self.higiene < 0:
            self.higiene = 0
        elif self.higiene > 100:
            self.higiene = 199

        if self.felicidade < 0:
            self.felicidade = 0
        elif self.felicidade > 100:
            self.felicidade = 100

        if self.saude_fisica < 0:
            self.saude_fisica = 0
        elif self.saude_fisica > 100:
            self.saude_fisica = 100

        if self.saude_mental < 0:
            self.saude_mental = 0
        elif self.saude_mental > 100:
            self.saude_mental = 100

    # AQUI É CRIADO O METODO PARA VERIFICAR SE O PET IRA MORRER DE FOME OU NÃO
    def verificar_fome(self):

        if self.fome == 0:
            self.vivo = False
            mortes_fome = [
                "morreu seco de fome.",
                "morreu de buxin vazi.",
                "morreu magro.",
            ]
            morte = random.choice(mortes_fome)
            print("{} {}".format(self.nome, morte))
            return False
        return True

    # AQUI É CRIADO O METODO PARA VERIFICAR SE O PET IRA MORRER DE HIGIENE OU NÃO
    def verificar_higiene(self):

        if self.higiene == 0:
            self.vivo = False
            mortes_higiene = [
                "morreu todo podre.",
                "morreu fedendo.",
                "morreu de desgosto próprio.",
            ]
            morte = random.choice(mortes_higiene)
            print("{} {}".format(self.nome, morte))
            return False
        return True

    # AQUI É CRIADO O METODO PARA VERIFICAR SE O PET IRA MORRER DE TRISTEZA OU NÃO
    def verificar_felicidade(self):

        if self.felicidade == 0:
            self.vivo = False
            mortes_felicidade = [
                "morreu de depressão.",
                "morreu de infelicidade.",
                "morreu por amar demais quem não lhe ama de volta.",
            ]
            morte = random.choice(mortes_felicidade)
            print("{} {}".format(self.nome, morte))
            return False
        return True

    # AQUI É CRIADO O METO PARA VERIFICAR COMO ESTÁ A SAUDE FISÍCA DO PET
    def verificar_saudefisica(self):

        if self.saude_fisica == 0:
            self.vivo = False
            mortes_saudefisica = [
                "morreu imenso.",
                "morreu de forma precária.",
                "morreu fodido.",
            ]
            morte = random.choice(mortes_saudefisica)
            print("{} {}".format(self.nome, morte))
            return False
        return True

    # AQUI É CRIADO PARA VERIFICAR A SAUDE MENTAL DO PET
    def verificar_saudemental(self):

        if self.saude_mental == 0:
            self.vivo = False
            mortes_saudemental = [
                "morreu esgotado.",
                "morreu mal demais.",
                "morreu finado.",
            ]
            morte = random.choice(mortes_saudemental)
            print("{} {}".format(self.nome, morte))
            return False
        return True

    # AQUI É CRIADO O METODO DE STATUS PARA MOSTRAR NO PROGRAMA PRINCIPAL COMO O PET ESTÁ
    def status(self):
        print("Nome: {}".format(self.nome))
        print("Fome: {}".format(self.fome))
        print("Higiene: {}".format(self.higiene))
        print("Felicidade: {}".format(self.felicidade))
        print("Saúde mental: {}".format(self.saude_mental))
        print("Saúde fisíca: {}".format(self.saude_fisica))

    def alimentar_pet(self):
        self.alimentar()
        self.update_status()

    def banhar_pet(self):
        self.alimentar()
        self.update_status()

    def fumar_pet(self):
        self.fumar()
        self.update_status()

    def brincar_pet(self):
        self.brincar()
        self.update_status()

    def abandonar_pet(self):
        resultado = random.choice([
            "Você é um otário por abandonar {}.".format(self.nome),
            "Parabéns, seu desprezível.",
            "Espero que sofra por abandona-lo."
        ])
        messagebox.showinfo("Resultado", resultado)
        root.destroy()
# AQUI É O CÓDIGO PRINCIPAL QUE RODA O PROGRAMA


def main():

    # AQUI É ONDE DEFINIMOS O NOME DO PET E SERÁ USADO O RESTO DO CODIGO
    nome_pet = input("Nomeie o seu pet: ").capitalize()
    pet = VirtualPet(nome_pet)

    # AQUI É ONDE O PROGRAMA COMEÇA REALMENTE A FUNCIONAR
    while True:
        print("\nO que deseja fazer com o(a) {}".format(nome_pet))
        print("1 - Alimente o(a) {}".format(nome_pet))
        print("2 - Dê banho no(a) {}".format(nome_pet))
        print("3 - Dê um cigarrin pra {}".format(nome_pet))
        print("4 - Brincar com {}".format(nome_pet))
        print("5 - Veja como {} está".format(nome_pet))
        print("6 - ABANDONE {}".format(nome_pet))

        # AQUI ELE PEDE A OPÇÃO PARA SEGUIR COM O PROGRAMA
        escolha = input("Escolha uma opção (1-6): ")
        print("")

        # SE ESCOLHER 1, O PET SERÁ ALIMENTADO
        if escolha == "1":
            pet.alimentar()

            if pet.fome == 100:
                print("{} não aguenta mais comer.".format(nome_pet))
            else:
                print("{} está de buxo chei.".format(nome_pet))

        # SE ESCOLHER 2, O PET SERÁ BANHADO
        elif escolha == "2":
            pet.banhar()

            if nome_pet == "Jean":
                print("{} não curte isso pois coça.".format(nome_pet))
            else:
                print("{} está limpim.".format(nome_pet))

        # SE ESCOLHER 3, O PET IRÁ FUMAR CIGARRO
        elif escolha == "3":
            pet.fumar_um()

            if nome_pet == "Jean":
                print("{} FUMOU O TAL DO CIGARRO DE CRAVO.".format(nome_pet))
            else:
                print("{} apreciou um cigarretes after sex.".format(nome_pet))

        # SE ESCOLHER 4, O PET VAI BRINCAR
        elif escolha == "4":
            pet.brincar()

            print("{} brincou com o palhaço.".format(nome_pet))

        # SE ESCOLHER 5, O PROGRAMA VAI MOSTRAR COMO ESTÃO OS STATUS ATUAIS DO PET E VERIFICAR SE ELE MORREU
        elif escolha == "5":
            pet.status()
            pet.verificar_fome()
            pet.verificar_felicidade()
            pet.verificar_higiene()
            pet.verificar_saudefisica()
            pet.verificar_saudemental()

        # SE ESCOLHER 6, O PET VAI SER ABANDONADO E O PROGRAMA PARA
        elif escolha == "6":
            abandonos = [
                "Você é um otario por abandonar {}.".format(nome_pet),
                "Parabéns, seu desprezível.",
                "Espero que sofra por abandona-lo.",
            ]
            resultado = random.choice(abandonos)
            print("{}".format(resultado))
            break

        # SE COLOCA ALGUM NÚMERO MENOR QUE 1 OU MAIOR QUE 6, O PROGRAMA DÁ ERRO E PEDE PARA INSERIR OUTRA OPÇÃO
        else:
            print("Não existe essa opção.")


if __name__ == "__main__":
    main()
