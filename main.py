# Exercício Avaliativo AV2 - Python

# 1. (Dados Aglomerados) Desenvolva um programa em Python que cadastre informações de várias
# pessoas (nome, idade e CPF) e depois coloque em um dicionário. Depois remova todas as
# pessoas menores de 18 anos do dicionário e coloque em outro dicionário. (1,0 ponto).
qtdPessoas = int(input("Quantas pessoas você deseja cadastrar? "))
pessoas = {}
for i in range(qtdPessoas):
    pessoa = {}
    pessoa["nome"] = input("Digite o nome da pessoa: ")
    pessoa["idade"] = int(input("Digite a idade da pessoa: "))
    pessoa["cpf"] = input("Digite o CPF da pessoa: ")
    pessoas[i] = pessoa
maiores = {}
menores = {}
for pessoa_id, pessoa_info in pessoas.items():
    if pessoa_info["idade"] < 18:
        menores[pessoa_id] = pessoa_info
    else:
        maiores[pessoa_id] = pessoa_info
print("\nPessoas maiores de 18 anos:")
for pessoa_id, pessoa_info in maiores.items():
    print(f"ID: {pessoa_id}, Nome: {pessoa_info['nome']}, Idade: {pessoa_info['idade']}, CPF: {pessoa_info['cpf']}")
print("\nPessoas menores de 18 anos:")
for pessoa_id, pessoa_info in menores.items():
    print(f"ID: {pessoa_id}, Nome: {pessoa_info['nome']}, Idade: {pessoa_info['idade']}, CPF: {pessoa_info['cpf']}")


# 2. (Dados Aglomerados) Considere um sistema Python onde os dados são armazenados em
# dicionários. Nesse sistema existe um dicionario principal e o dicionário de backup. Cada vez
# que o dicionário principal atinge tamanho 5, ele imprime os dados na tela e apaga o seu conteúdo.
# Crie um programa que insira dados em um dicionário, realizando o backup a cada dado e
# excluindo os dados do dicionário principal quando ele atingir tamanho 5. (1,0 ponto).
# dados = {}
# backup = {}
# print("Inserção de Dados")
# while True:
#     chave = input("Digite a chave: ")
#     valor = input("Digite o valor: ")
#     dados[chave] = valor
#     if(len(dados) >= 5):
#         backup.update(dados)
#         print("Backup realizado:")
#         print(backup)
#         dados.clear()


# 3. (Prog. Orientado Objetos) Elabore um programa em Python que Crie a classe “Automóvel” e
# derive (Herança) as 4 subclasses abaixo,"Carro", "Caminhao", "Caminhonete", "Moto". Seu programa deve ter no mínimo 2 atributos e no
# mínimo 2 métodos (e garantir o Polimorfismo). (1,5 pontos).
# class Automovel():
#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
#     def vecolidade_maxima(self):
#         pass
#     def quilometragem_por_Litro(self):
#         pass

# class Carro(Automovel):
#     def __init__(self, marca, modelo, ano):
#         super().__init__(marca, modelo, ano)
#     def velocidade_maxima(self):
#         print(f"A velocidade máxima do {self.marca} {self.modelo} é 200KM/h")
#     def quilometragem_por_Litro(self):
#         print(f"A quilometragem por litro em média do {self.modelo} é 15KM/l")

# class Caminhao(Automovel):
#     def __init__(self, marca, modelo, ano):
#         super().__init__(marca, modelo, ano)
#     def velocidade_maxima(self):
#         print(f"A velocidade máxima do {self.marca} {self.modelo} é 110/h")
#     def quilometragem_por_Litro(self):
#         print(f"A quilometragem por litro em média do {self.modelo} é 8KM/l")

# class Caminhonete(Automovel):
#     def __init__(self, marca, modelo, ano):
#         super().__init__(marca, modelo, ano)
#     def velocidade_maxima(self):
#         print(f"A velocidade máxima do {self.marca} {self.modelo} é 150/h")
#     def quilometragem_por_Litro(self):
#         print(f"A quilometragem por litro em média do {self.modelo} é 11KM/l")

# class Moto(Automovel):
#     def __init__(self, marca, modelo, ano):
#         super().__init__(marca, modelo, ano)
#     def velocidade_maxima(self):
#         print(f"A velocidade máxima do {self.marca} {self.modelo} é 230/h")
#     def quilometragem_por_Litro(self):
#         print(f"A quilometragem por litro em média do {self.modelo} é 21KM/l")

# while True:
#     print("\n(1)Carro\n(2)Caminhao\n(3)Caminhonete\n(4)Moto\n(5)Encerrar Pesquisa")
#     tipo = int(input("Qual modelo deseja fazer uma pesquisa? "))
#     if(tipo == 1):
#         marca = input("\nDigite a marca: ")
#         modelo = input("Digite o modelo: ")
#         ano = int(input("Digite o ano: "))
#         pesquisa = Carro(marca, modelo, ano)
#         pesquisa.velocidade_maxima()
#         pesquisa.quilometragem_por_Litro()
#     elif(tipo == 2):
#         marca = input("\nDigite a marca: ")
#         modelo = input("Digite o modelo: ")
#         ano = int(input("Digite o ano: "))
#         pesquisa = Caminhao(marca, modelo, ano)
#         pesquisa.velocidade_maxima()
#         pesquisa.quilometragem_por_Litro()
#     elif(tipo == 3):
#         marca = input("\nDigite a marca: ")
#         modelo = input("Digite o modelo: ")
#         ano = int(input("Digite o ano: "))
#         pesquisa = Caminhonete(marca, modelo, ano)
#         pesquisa.velocidade_maxima()
#         pesquisa.quilometragem_por_Litro()
#     elif(tipo == 4):
#         marca = input("\nDigite a marca: ")
#         modelo = input("Digite o modelo: ")
#         ano = int(input("Digite o ano: "))
#         pesquisa = Moto(marca, modelo, ano)
#         pesquisa.velocidade_maxima()
#         pesquisa.quilometragem_por_Litro()
#     elif(tipo == 5):
#         print("\nPrograma encerrado!")
#         break
#     else:
#         print("\nOpção Invalida!")
    

# 4. (Prog. Orientado Objetos) Elabore um programa em Python que Crie a classe “Produto” e derive
# (Herança) as 3 subclasses abaixo, "Livro", "CD", "DVD". Seu programa deve ter no mínimo 3 atributos e no mínimo 2
# métodos (e garantir o Polimorfismo). O programa deve ter um menu que escolha qual classe o
# usuário quer instanciar. (1,5 pontos).
# class Produto():
#     def __init__(self, nome, valor, anoLancamento):
#         self.nome = nome
#         self.valor = valor
#         self.anoLancamento = anoLancamento
#     def informacoes(self):
#         pass
#     def desconto(self):
#         pass
# class Livro(Produto):
#     def __init__(self, nome, valor, anoLancamento):
#         super().__init__(nome, valor, anoLancamento)
#     def informacoes(self):
#         print(f"Nome do Livro: {self.nome}, Ano de Lancamento: {self.anoLancamento}, Valor: R${self.valor}")
#     def desconto(self):
#         self.valor = self.valor - (self.valor*(5 / 100))
#         print(f"Esse livro tem desconto de 5%\nValor Atualizado: R${self.valor}")
# class CD(Produto):
#     def __init__(self, nome, valor, anoLancamento):
#         super().__init__(nome, valor, anoLancamento)
#     def informacoes(self):
#         print(f"Nome do CD: {self.nome}, Ano de Lancamento: {self.anoLancamento}, Valor: R${self.valor}")
#     def desconto(self):
#         self.valor = self.valor - (self.valor*(2 / 100))
#         print(f"Esse CD tem desconto de 2%\nValor Atualizado: R${self.valor}")
# class DVD(Produto):
#     def __init__(self, nome, valor, anoLancamento):
#         super().__init__(nome, valor, anoLancamento)
#     def informacoes(self):
#         print(f"Nome do DVD: {self.nome}, Ano de Lancamento: {self.anoLancamento}, Valor: R${self.valor}")
#     def desconto(self):
#         self.valor = self.valor - (self.valor*(7 / 100))
#         print(f"Esse DVD tem desconto de 7%\nValor Atualizado: R${self.valor}")
# while True:
#     print("\n(1)Livro\n(2)CD\n(3)DVD\n(4)Encerrar")
#     opcao = int(input("Qual opção deseja fazer? "))
#     if(opcao == 1):
#         nome = input("\nDigite o nome: ")
#         valor = int(input("Digite o valor: "))
#         ano = int(input("Digite o ano de lancamento: "))
#         livro = Livro(nome, valor, ano)
#         livro.informacoes()
#         livro.desconto()
#     elif(opcao == 2):
#         nome = input("\nDigite o nome: ")
#         valor = int(input("Digite o valor: "))
#         ano = int(input("Digite o ano de lancamento: "))
#         cd = CD(nome, valor, ano)
#         cd.informacoes()
#         cd.desconto()
#     elif(opcao == 3):
#         nome = input("\nDigite o nome: ")
#         valor = int(input("Digite o valor: "))
#         ano = int(input("Digite o ano de lancamento: "))
#         dvd = DVD(nome, valor, ano)
#         dvd.informacoes()
#         dvd.desconto()
#     elif(opcao == 4):
#         print("\nPrograma encerrado!")
#         break
#     else:
#         print("\nOpção Invalida!")
