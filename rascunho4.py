senha = 1234
tentativa = 3

while tentativa > 0:
    digito = int(input("digite a senha: "))
    if digito == senha:
        print("senha correta!")
        tentativa -= 3
    else:
        print("senha incorreta.")
        tentativa -= 1
        if tentativa == 0:
            print("acesso negado.")









