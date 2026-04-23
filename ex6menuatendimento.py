print("Bem vindo(a)!")
menu = input("""Digite a opção desejada:
             
            1.Ver extrato
            2.Conversar com um atendente
            3.Cancelar conta
            4.Opção inválida
""")

if menu == "1":
    print("O extrato estará disponível em seu e-mail")
elif menu == "2":
    print("Um funcionário entrará em contato pelo telefone!")
elif menu == "3":
    print("Não aceitamos o cancelamento da sua conta :)")
else:
    print("Escolha uma opção válida!")


