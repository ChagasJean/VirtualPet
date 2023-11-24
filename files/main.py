class VirtualPet:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 100
        self.higiene = 100
        self.felicidade = 100

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
        print(f"Nome: {self.nome}")
        print(f"Fome: {self.fome}")
        print(f"Higiene: {self.higiene}")
        print(f"Felicidade: {self.felicidade}")


def main():
    nome_pet = input("Nomeie o seu pet: ")
    pet = VirtualPet(nome_pet)

    while True:
        print("\nO que deseja fazer com o(a) {}".format(nome_pet))
        print("1 - Alimente o(a) {}".format(nome_pet))
        print("2 - Dê banho no(a) {}".format(nome_pet))
        print("3 - Brincar com {}".format(nome_pet))
        print("4 - Veja como {} está".format(nome_pet))
        print("5 - ABANDONE {}".format(nome_pet))

        escolha = input("Escolha uma opção: (1-5)")

        if escolha == "1":
            pet.alimentar()
        elif escolha == "2":
            pet.banhar()
        elif escolha == "3":
            pet.brincar()
        elif escolha == "4":
            pet.status()
        elif escolha == "5":
            print("Pensei que poderia te fazer mais feliz...")
            break
        else:
            print("Não existe essa opção.")


if __name__ == "__main__":
    main()
