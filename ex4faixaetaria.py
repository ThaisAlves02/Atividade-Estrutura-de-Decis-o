idade = int(input("Digite a sua idade: "))
if idade > 0 and idade < 17:
    print("Criança")
elif idade >= 18 and idade <= 59:
    print("Adulto")
elif idade > 60:
    print("Sênior")
else:
    print("Alienígena")