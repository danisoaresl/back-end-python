# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.

# 1. Cada conta corrente pode ter um ou mais clientes como titular.
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela 
#    fizer um depósito, aumentaremos o saldo.
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda
#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até
#    -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.

# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança", "propriedades", "encapsulamento" e "classe abstrata".



from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, nome, telefone, renda_mensal):
        self.nome = nome
        self.telefone = telefone
        self.renda_mensal = renda_mensal

    @abstractmethod
    def calcular_cheque_especial(self):
        pass

class ClienteMulher(Cliente):
    def calcular_cheque_especial(self):
        return -self.renda_mensal

class ClienteHomem(Cliente):
    def calcular_cheque_especial(self):
        return 0  # Homens não têm direito a cheque especial por enquanto

class ContaCorrente:
    def __init__(self):
        self.saldo = 0
        self.operacoes = []

    def realizar_deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(f'Depósito: +{valor}')

    def realizar_saque(self, valor, cliente):
        limite_cheque_especial = cliente.calcular_cheque_especial()
        if self.saldo - valor >= limite_cheque_especial:
            self.saldo -= valor
            self.operacoes.append(f'Saque: -{valor}')
        else:
            print("Saque não permitido. Saldo insuficiente.")

# Exemplo de uso do sistema
cliente_mulher = ClienteMulher(nome="Ana", telefone="123456789", renda_mensal=5000)
cliente_homem = ClienteHomem(nome="João", telefone="987654321", renda_mensal=6000)

conta_ana = ContaCorrente()
conta_joao = ContaCorrente()

conta_ana.realizar_deposito(2000)
conta_joao.realizar_deposito(1500)

conta_ana.realizar_saque(3000, cliente_mulher)  # Saque permitido usando cheque especial
conta_joao.realizar_saque(2000, cliente_homem)  # Saque permitido sem cheque especial

print(f"Saldo da conta de Ana: {conta_ana.saldo}")
print(f"Saldo da conta de João: {conta_joao.saldo}")



#Neste modelo:

#Cliente é uma classe abstrata que define as propriedades comuns a todos os clientes.
#ClienteMulher e ClienteHomem são subclasses de Cliente que implementam o método abstrato calcular_cheque_especial de acordo com as regras específicas para mulheres e homens.
#ContaCorrente representa a conta corrente e possui métodos para realizar depósitos e saques. O método realizar_saque verifica se o saque é permitido de acordo com o saldo e o cheque especial disponível.





