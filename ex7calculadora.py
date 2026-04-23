n1 = float(input("Digite o número 1: "))
n2 = float(input("Digite o número 2: "))
operador = input("""
                 Digite o número da operação desejada:
                 1.Soma 
                 2.Subtração
                 3.Multiplicação 
                 4.Divisão           
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
elif operador == "4":
    if n2 == 0:
        resultado = "TENTATIVA DE DIVISÃO POR 0"
    else:
        resultado = n1 / n2
    
    print(f"Resultado: {resultado}")

else:
    resultado = "OPERAÇÃO INVÁLIDA"