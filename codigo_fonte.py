#Display De Navegação NCSA
#//
#//
import json



with open("dados_colonia.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
nomes_modulos = [modulo["nome"] for modulo in dados["modulos"]]

exibir_nome_modulos = lambda nomes: [print(f"- {nome}") for nome in nomes]


# Exemplo de acesso a um dado específico:
# primeiro_modulo = dados["modulos"][0]
# print(primeiro_modulo["nome"])
# print(primeiro_modulo["status"])

    print("\n********* MÓDULOS DA COLÔNIA ************")

    def exibir_modulos(nomes_modulos):
        for nome in nomes_modulos:
            print(f"- {nome}")
    print("Dados da Colônia carregados com sucesso.")
    print("Quantidade de módulos: ", len(dados["modulos"]))

print("==============================================")
print("       NCSA - AURORA SIGER")
print("       Núcleo Cognitivo da Colônia")
print("==============================================")


opcao = ""

while opcao != "0":

    print()
    print("[1] Visualizar módulos")
    print("[2] Consultar histórico")
    print("[3] Analisar alerta")
    print("[4] Executar validação lógica")
    print("[5] Exibir prompts")
    print("[6] Simular assistente IA")
    print("[0] Encerrar")
    print("\n")

    opcao = input("Escolha uma opção: ")
    print("Você escolheu a opção: ", opcao)

    if opcao == "1":
        print("Visualização de módulos selecionada.")
        exibir_modulos(nomes_modulos)
    elif opcao == "2":
        print("Consulta de histórico selecionada.")
    elif opcao == "3":
        print("Análise de alertas selecionada.")
    elif opcao == "4":
        print("Validação lógica selecionada.")  
    elif opcao == "5":
        print("Exibição de prompts selecionada.")
    elif opcao == "6":
        print("Simulação de assistente IA selecionada.")
    elif opcao == "0":
        print("Encerrando o NCAS...")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

    #print(dados) 




