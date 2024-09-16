rep = 1
while rep != 2:
    aluno = int(input("informe o numero de alunos: "))

    cont = 0
    soma = 0

    while cont < aluno :
        notas = int(input("informe as notas: "))
        cont += 1
        soma = soma+notas

    media = soma/aluno
    print(f'resultado {media}')
    rep = int(input("deseja repetir?\n"
                    "1 para sim\n"
                    "2 para nao: "))
