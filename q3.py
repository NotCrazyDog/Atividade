nome = input('Digite o nome do cidadão: ')
idade = int(input('Digite a idade do cidadão: '))
if idade >= 16:
    print(f"{nome} está apto a votar.")
else:
    print(f"{nome} NÃO está apto a votar.")