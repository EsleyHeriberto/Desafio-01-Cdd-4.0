class Pessoa():
    def __init__(self, nome, peso, idade, comendo=False, falando=False, dormindo=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.dormindo = dormindo

# metodos: comer, dormir e falar
# contra-metodos: pararComer, acordar e pararFalar

    def falar(self, falando):
        if self.comendo:
            print(f"{self.nome} não pode falar enquanto come.")
            return

        if self.dormindo:
            print(f"{self.nome} não tem como falar enquanto dorme.")
            return

        if self.falando:
            print(f"{self.nome} já está falando.")
            return

        print(f"{self.nome} está falando que {falando}")
        self.falando = True

    def pararFalar(self):
        if not self.falando:
            print(f"{self.nome} não está falando.")
            return

        print(f"{self.nome} parou de falar.")
        self.falando = False

    def comer(self, alimento, bebida):
        if self.comendo:
            print(f"{self.nome} já está comendo.")
            return

        if self.falando:
            print(f"{self.nome} não pode comer falando.")
            return

        if self.dormindo:
            print(f"{self.nome} não tem como comer dormindo.")
            return

        print(f"{self.nome} está comendo {alimento} e bebendo {bebida}.")
        self.comendo = True

    def pararComer(self):
        if not self.comendo:
            print(f"{self.nome} não está comendo.")
            return

        print(f"{self.nome} parou de comer.")
        self.comendo = False

    def dormir(self):
        if self.dormindo:
            print(f"{self.nome} já está dormindo.")
            return

        if self.falando:
            print(f"{self.nome} não pode dormir falando.")
            return

        if self.comendo:
            print(f"{self.nome} não pode dormir se estiver comendo.")
            return

        print(f"{self.nome} está dormindo...")
        self.dormindo = True

    def acordar(self):
        if not self.dormindo:
            print(f"{self.nome} não está dormindo.")
            return

        print(f"{self.nome} acordou.")
        self.dormindo = False
