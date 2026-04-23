print("Bem vindo(a) á Lanchonete do Python!")
print("""
                      Catálogo da lanchonete
    ------------------------------------------------------------
    | Código |      Produto      |  Preço   |    Categoria     |
    |  001   | X-Buguer          | R$ 18,00 | Lanches          |
    |  002   | X-Salada          | R$ 20,00 | Lanches          |
    |  003   | X-Bacon           | R$ 22,00 | Lanches          |
    |  004   | Hot Dog Simples   | R$ 12,00 | Lanches          |
    |  005   | Hot Dog Especial  | R$ 16,00 | Lanches          |
    |  006   | Batata Frita P    | R$ 9,00  | Acompanhamentos  |
    |  007   | Batata Frita G    | R$ 14,00 | Acompanhamentos  |
    |  008   | Onion Rings       | R$ 11,00 | Acompanhamentos  |
    |  009   | Refrigerante Lata | R$ 6,00  | Bebidas          |
    |  010   | Suco Natural      | R$ 8,00  | Bebidas          |
    |  011   | Milk Shake        | R$ 15,00 | Bebidas          |
    |  012   | Sorvete 2 Bolas   | R$ 10,00 | Sobremesas       |
    ------------------------------------------------------------
""")
codigoProd = (input("Digite o código do produto desejado: "))
qtd = int(input("Digite a quantidade do produto: "))
preco = 0
nomeProd = ""
if codigoProd == "001":
   nomeProd = "X-Buguer" 
   preco = 18
elif codigoProd == "002":
   nomeProd = "X-Salada" 
   preco = 20
elif codigoProd == "003":
   nomeProd = "X-Bacon" 
   preco = 22
elif codigoProd == "004":
   nomeProd = "Hot Dog Simples" 
   preco = 12
elif codigoProd == "005":
   nomeProd = "Hot Dog Especial" 
   preco = 16
elif codigoProd == "006":
   nomeProd = "Batata Frita P" 
   preco = 9
elif codigoProd == "007":
   nomeProd = "Batata Frita G" 
   preco = 14
elif codigoProd == "008":
   nomeProd = "Onion Rings" 
   preco = 11
elif codigoProd == "009":
   nomeProd = "Refrigerante Lata" 
   preco = 6
elif codigoProd == "010":
   nomeProd = "Suco Natural" 
   preco = 8
elif codigoProd == "011":
   nomeProd = "Milk Shake" 
   preco = 15
elif codigoProd == "012":
   nomeProd = "Sorvete 2 Bolas" 
   preco = 10
else:
   print("Erro! O código que você escolheu não existe no nosso catálogo.")

valorTotal = preco * qtd
print(f"""
    ---- Resumo do pedido ----
    Produto: {nomeProd}
    Preço unitário: R$ {preco}
    Quantidade: {qtd}
    Total á pagar: R$ {valorTotal:.2f}
    Obrigado pela preferência!
""")