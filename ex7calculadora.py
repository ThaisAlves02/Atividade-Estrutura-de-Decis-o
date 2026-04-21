n1 = float(input("Digite o número 1: "))
n2 = float(input("Digite o número 2: "))
operador = input("""
                 Digite a operação desejada:
                 1.Soma
                 2.Subtração
                 3.Multiplicação
                 4.Divisao
        ----------------------------------------------             
""")
if operador == "1":
    resultado = n1 + n2
    print(f"Resultado: {resultado}")
elif operador == "2":
    resultado = n1 - n2
    print(f"Resultado: {resultado}")
elif operador == "3":
    resultado = n1 * n2
    print(f"Resultado: {resultado}")
else:
    resultado = n1 / n2
    print(f"Resultado: {resultado}")