# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.



# Crie uma instância da classe carro.


# Faça o carro "andar" utilizando os métodos da sua classe.


# Faça o carro "parar" utilizando os métodos da sua classe.


class Carro:
    def __init__(self, cor, modelo):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0

    def liga(self):
        if not self.ligado:
            self.ligado = True
            print("O carro está ligado.")
        else:
            print("O carro já está ligado.")

    def desliga(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
            print("O carro está desligado.")
        else:
            print("O carro já está desligado.")

    def acelera(self, incremento):
        if self.ligado:
            self.velocidade += incremento
            print(f"O carro acelerou. Velocidade atual: {self.velocidade} km/h.")
        else:
            print("Não é possível acelerar. O carro está desligado.")

    def desacelera(self, decremento):
        if self.ligado and self.velocidade >= decremento:
            self.velocidade -= decremento
            print(f"O carro desacelerou. Velocidade atual: {self.velocidade} km/h.")
        elif self.ligado:
            self.velocidade = 0
            print("O carro parou.")
        else:
            print("Não é possível desacelerar. O carro está desligado.")

# Criando uma instância da classe Carro
meu_carro = Carro(cor="azul", modelo="sedan")

# Ligando o carro
meu_carro.liga()

# Acelerando o carro
meu_carro.acelera(20)

# Desacelerando o carro
meu_carro.desacelera(10)

# Parando o carro
meu_carro.desliga()


