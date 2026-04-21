preco = float(input("Digite o preço do produto: "))
qtd = int(input("Digite a quantidade do produto: "))
valorTotal = preco * qtd
desconto1 = 0.15
desconto2 = 0.1
if valorTotal > 100 or qtd >= 5:
   resultado = valorTotal * desconto1
   print(f"""
         Valor Original: {valorTotal}
         Valor á ser pago: {resultado}         
""")
elif valorTotal <= 100 and qtd >= 3:
   resultado = valorTotal * desconto2
   print(f"""
         Valor Original: {valorTotal}
         Valor á ser pago: {resultado}         
""")
else:
   print(f"Sem desconto. O valor total á pagar é {valorTotal}")