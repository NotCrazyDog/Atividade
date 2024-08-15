n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print(f"{n1} + {n2} = {n1+n2}")
print(f"{n1} - {n2} = {n1-n2}")
print(f"{n1} . {n2} = {n1*n2}")
if n2 == 0:
    print("não é posível dividir por 0")
else:
    print(f"{n1} / {n2} = {n1/n2}")
    
