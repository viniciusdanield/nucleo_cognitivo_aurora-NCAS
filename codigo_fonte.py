#Display De Navegação NCSA
#//
#//

print("==============================================")
print("       NCSA - AURORA SIGER")
print("       Núcleo Cognitivo da Colônia")
print("==============================================")


opcao = ""

while opcao != "0":

    print()
    print("[1] Cadastrar registro")
    print("[2] Consultar registro")
    print("[3] Visualizar módulos")
    print("[4] Analisar alerta")
    print("[5] Executar validação lógica")
    print("[6] Exibir prompts")
    print("[7] Simular assistente IA")
    print("[0] Encerrar")
    print("\n")

    opcao = input("Escolha uma opção: ")
    print("Você escolheu a opção: ", opcao)

    if opcao == "1":
        print("Cadastro de registros selecionado.")
    elif opcao == "2":
        print("Consulta de registros selecionada.")
    elif opcao == "3":
        print("Visualização de módulos selecionada.")
    elif opcao == "4":
        print("Análise de alertas selecionada.")
    elif opcao == "5":
        print("Validação lógica selecionada.")  
    elif opcao == "6":
        print("Exibição de prompts selecionada.")
    elif opcao == "7":
        print("Simulação de assistente IA selecionada.")
    elif opcao == "0":
        print("Encerrando o NCAS...")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")




