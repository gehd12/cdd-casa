op = 1
while op !=2:
    nota1 = float(input('informe a primeira nota: '))
    while nota1 < 0 or nota1 > 10:
        print('informe uma nota diferente! ')
        nota1 = float(input('informe a primeira nota: '))

    nota2 = float(input('informe a segunda nota: '))
    while nota2 < 0 or nota2 > 10:
        print('informe uma nota diferente! ')
        nota2 = float(input('informe a primeira nota: '))

    media = (nota1 + nota2) / 2
    print(f'a media do aluno foi {media}')

    op = int(input('deseja fazer um novo calculo?\n'
          '1 para sim\n'
          '2 para nao: '))