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
            print(f"Integridade: {modulo['integridade_percentual']}%")
            print(f"Falha Crítica:{modulo['falha_critica']}")

            encontrou_alerta = True
    
    if not encontrou_alerta:
        print("Nenhum alerta encontrado.")

def validar_alerta(modulo):
    falha_critica = modulo["falha_critica"]
    status_alerta = modulo["status"] == "alerta"
    integridade_baixa = modulo["integridade_percentual"] < 80

    risco = falha_critica or status_alerta or integridade_baixa
    
    return risco

def mostrar_simplificacao():
    print("\n*********** SIMPLIFICAÇÃO BOOLEANA ************")

    print("\nExpressão original:")
    print("R = (F AND A) OR (F AND NOT A) OR I")

    print("\nAplicando distributividade:")
    print("R = F AND (A OR NOT A) OR I")

    print("\nPela lei do terceiro excluído:")
    print("A OR NOT A = True")

    print("\nExpressão simplificada:")
    print("R = F OR I")

def executar_validacao_logica():
    print("\n********* VALIDAÇÃO LÓGICA ************")
    
    print("\nRegra utilizada")
    print("RISCO = falha_critica OR status_alerta OR integridade_baixa")

    for modulo in dados["modulos"]:

        falha_critica = modulo["falha_critica"]
        status_alerta = modulo["status"] == "alerta"
        integridade_baixa = modulo["integridade_percentual"] < 80

        risco = falha_critica or status_alerta or integridade_baixa

        print(f"\nMódulo: {modulo['nome']}")
        print(f"Falha Crítica: {falha_critica}")    
        print(f"Status é alerta: {status_alerta}")
        print(f"Integridade abaixo de 80%: {integridade_baixa}")
        print(f"Resultado de risco: {risco}")

def exibir_prompts():
    print("\n********* PROMPTS DO NCAS ************")

    prompt_zero_shot = """ 
Você é o assistente operacional da colônia Aurora Siger.
Analise os dados fornecidos e identifique possíveis riscos operacionais.
Apresente um resumo e uma recomendação de ação.   
"""

    prompt_few_shot = """
Você é o assistente operacional da colônia Aurora Siger.

Exemplo:
Entrada: módulo com integridade de 70%.
Saída: risco identificado devido à baixa integridade.

Agora analise os dados dos módulos da colônia
e identifique situações que exigem atenção.
"""
    prompt_estruturado = """
Analise os dados operacionais da colônia e responda
utilizando a seguinte estrutura:

{
    "prioridade": "",
    "risco": "",
    "resumo": "",
    "recomendacao": "",
    "acao_humana": ""
}
"""
    print("\nPrompt Zero-Shot:")
    print(prompt_zero_shot)

    print("\nPrompt Few-Shot:")
    print(prompt_few_shot)

    print("\nPrompt Estruturado:")
    print(prompt_estruturado)



print("==============================================")
print("       NCSA - AURORA SIGER")
print("       Núcleo Cognitivo da Colônia")
print("==============================================")


opcao = ""

while opcao != "0":

    print()
    print("[1] Visualizar módulos")
    print("[2] Consultar histórico")
    print("[3] Analisar alertas")
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
        analisar_alerta() 
    elif opcao == "4":
        print("Validação lógica selecionada.")
        executar_validacao_logica()
        mostrar_simplificacao()
    elif opcao == "5":
        exibir_prompts()
    elif opcao == "6":
        print("Simulação de assistente IA selecionada.")
    elif opcao == "0":
        print("Encerrando o NCAS...")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

    #print(dados) 





