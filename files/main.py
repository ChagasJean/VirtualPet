class VirtualPet:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.higiene = 0
        self.felicidade = 0

    def alimentar(self):
        self.fome += 10
        self.higiene -= 5
        self.felicidade += 5
        self.verificar_limites()

    def banhar(self):
        self.higiene += 15
        self.fome -= 5
        self. felicidade += 5
        self.verificar_limites()

    def brincar(self):
        self.felicidade += 10
        self.fome -= 5
        self.higiene -= 5
        self.verificar_limites()

    def fumar_um(self):
        self.felicidade += 5
        self.fome -= 10
        self.higiene -= 5
        self.verificar_limites()

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

    def status(self):
        print("Nome: {}".format(self.nome))
        print("Fome: {}".format(self.fome))
        print("Higiene: {}".format(self.higiene))
        print("Felicidade: {}".format(self.felicidade))


def main():
    nome_pet = input("Nomeie o seu pet: ").capitalize()
    pet = VirtualPet(nome_pet)

    while True:
        print("\nO que deseja fazer com o(a) {}".format(nome_pet))
        print("1 - Alimente o(a) {}".format(nome_pet))
        print("2 - Dê banho no(a) {}".format(nome_pet))
        print("3 - Dê um cigarrin pra {}".format(nome_pet))
        print("4 - Brincar com {}".format(nome_pet))
        print("5 - Veja como {} está".format(nome_pet))
        print("6 - ABANDONE {}".format(nome_pet))

        escolha = input("Escolha uma opção (1-6): ")
        print("")

        if escolha == "1":
            pet.alimentar()

            if pet.fome == 100:
                print("{} não aguenta mais comer.".format(nome_pet))
            else:
                print("{} está de buxo chei.".format(nome_pet))

        elif escolha == "2":
            pet.banhar()

            if nome_pet == "Jean":
                print("{} não curte isso pois coça.".format(nome_pet))
            else:
                print("{} está limpim.".format(nome_pet))

        elif escolha == "3":
            pet.fumar_um()

            if nome_pet == "Jean":
                print("{} FUMOU O TAL DO CIGARRO DE CRAVO.".format(nome_pet))
            else:
                print("{} apreciou um cigarretes after sex.".format(nome_pet))

        elif escolha == "4":
            pet.brincar()

            print("{} brincou com o palhaço.".format(nome_pet))

        elif escolha == "5":
            pet.status()

        elif escolha == "6":
            print("Pensei que poderia te fazer mais feliz...")
            break

        else:
            print("Não existe essa opção.")


if __name__ == "__main__":
    main()
