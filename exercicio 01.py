litro=float(input('informe a quantidade de litros abestecido:'))
tipo= (input("informe o tipo de combustivel\n"
           "E ou e para etanol\n"
           "G ou g para gasolina: "))

if tipo == 'G' or tipo == 'g':
    valor=litro * 5.8
    print(f'total a pagar {valor}')

elif tipo == 'E' or tipo == 'e':
    valor2=litro * 4.90
    print(f"total a pagar {valor2}")
else:
    print('invalido')