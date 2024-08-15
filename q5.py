aluno = input('Digite o nome do aluno(a): ')
disci = input('Digite a disciplina: ')
nota = float(input('Digite a nota: '))

if nota >= 0 and nota <= 10:
    if nota >= 6:
        print(f'{aluno} está aprovado em {disci} com nota {nota}.')
    if nota >= 5.5 and nota < 6:
        print(f'{aluno} está aprovado em {disci} com nota 6.')
    if nota < 5.5:
        print(f'{aluno} NÃO está aprovado em {disci} com nota {nota}.')
else:
    print('Nota inválida, tente novamente.')
