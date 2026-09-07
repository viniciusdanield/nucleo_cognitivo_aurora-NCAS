#Display De Navegação NCSA
#//
#//
import json



with open("dados_colonia.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
nomes_modulos = [modulo["nome"] for modulo in dados["modulos"]]

with open("historico_colonia.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Sistema NCAS iniciado.\n")
    
# Exemplo de acesso a um dado específico:
# primeiro_modulo = dados["modulos"][0]
# print(primeiro_modulo["nome"])
# print(primeiro_modulo["status"])


def exibir_modulos(nomes_modulos):
    print("\n********* MÓDULOS DA COLÔNIA ************")
    print("Dados da Colônia carregados com sucesso.")
    print("Quantidade de módulos: ", len(dados["modulos"]))

    for nome in nomes_modulos:
         print(f"- {nome}")
def consultar_historico():
    print("\n********* HISTÓRICO DA COLÔNIA ************")

    with open("historico_colonia.txt", "r", encoding="utf-8") as arquivo:
        historico = arquivo.read()

    print(historico)

def registrar_historico(mensagem):
    with open("historico_colonia.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{mensagem}\n")

def analisar_alerta():
    print("\n********* ANÁLISE DE ALERTAS ************")

    encontrou_alerta = False

    for modulo in dados["modulos"]:
        if validar_alerta(modulo):
            print(f"ALERTA: {modulo['nome']}:")
            print(f"Status: {modulo['status']}")
            print(F"Falha Crítica:{modulo['falha_critica']}")
            encontrou_alerta = True
    
    if not encontrou_alerta:
        print("Nenhum alerta encontrado.")

def validar_alerta(modulo):
    falha_critica = modulo["Falha critica"]
    status_alerta = modulo["status"] == "alerta"

    if falha_critica or status_alerta:
        return True
    
    return False 

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
        registrar_historico("Usuário consultou os módulos da Colônia.")
        exibir_modulos(nomes_modulos)
    elif opcao == "2":
        print("Consulta de histórico selecionada.")
        registrar_historico("Usuário consultou o histórico da Colônia.")
        consultar_historico()
    elif opcao == "3":
        analisar_alerta(dados)
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





