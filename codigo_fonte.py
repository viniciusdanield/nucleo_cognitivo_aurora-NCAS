#Display De Navegação NCSA
#//
#//
import json
from ollama import chat


with open("dados_colonia.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

with open("registros_colonia.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Sistema NCAS iniciado.\n")
    
# Exemplo de acesso a um dado específico:
# primeiro_modulo = dados["modulos"][0]
# print(primeiro_modulo["nome"])
# print(primeiro_modulo["status"])


def exibir_modulos():
    print("\n********* MÓDULOS DA COLÔNIA ************")
    print("Dados da Colônia carregados com sucesso.")
    print("Quantidade de módulos: ", len(dados["modulos"]))

    for modulo in dados["modulos"]:
         print(f"- {modulo['nome']}")

def consultar_historico():
    print("\n********* HISTÓRICO DA COLÔNIA ************")

    with open("historico_colonia.txt", "r", encoding="utf-8") as arquivo:
        historico = arquivo.read()

    print(historico)

def registrar_historico(mensagem):
    with open("registros_colonia.txt", "a", encoding="utf-8") as arquivo:
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

def consultar_assistente_ia(modulo):
    prompt = f"""
Você é o assistente operacional da colônia Aurora Siger.

Analise os dados do módulo fornecidos pelo sistema NCAS.

IMPORTANTE:
- O sistema Python já identificou se existe risco.
- Não altere o resultado da análise lógica.
- Não invente informações que não estejam nos dados.
- Produza uma resposta objetiva.
- Não apresente seu raciocínio interno.
- Retorne somente um objeto JSON.

Dados do módulo:

Nome: {modulo["nome"]}
Categoria: {modulo["categoria"]}
Setor: {modulo["setor"]}
Status: {modulo["status"]}
Nível de importância: {modulo["nivel_importancia"]}
Consumo: {modulo["consumo_percentual"]}%
Capacidade: {modulo["capacidade_percentual"]}%
Temperatura: {modulo["temperatura"]}°C
Pressão: {modulo["pressao"]}
Integridade: {modulo["integridade_percentual"]}%
Falha crítica: {modulo["falha_critica"]}

Resultado da validação lógica do NCAS:
Risco identificado: {validar_alerta(modulo)}

Responda utilizando exatamente esta estrutura:

{{
    "modulo": "",
    "prioridade": "",
    "risco": "",
    "resumo": "",
    "recomendacao": "",
    "acao_humana": ""
}}
"""

    resposta = chat(
        model="qwen3:4b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return json.loads(resposta.message.content)

def cadastrar_registro():
    print("\n********* CADASTRO DE REGISTRO ************")

    nome = input("Nome do módulo: ")
    categoria = input("Categoria: ")
    setor = input("Setor: ")
    status = input("Status: ")
    nivel_importancia = input("Nível de importância: ")

    consumo = float(input("Consumo (%): "))
    capacidade = float(input("Capacidade (%): "))
    temperatura = float(input("Temperatura (°C): "))

    pressao_input = input("Pressão (deixe vazio se não se aplica): ")

    if pressao_input == "":
        pressao = None
    else:
        pressao = float(pressao_input)

    integridade = float(input("Integridade (%): "))

    falha_input = input("Falha crítica? (s/n): ").lower()

    if falha_input == "s":
        falha_critica = True
    else:
        falha_critica = False

    ultima_manutencao = input("Última manutenção: ")

    novo_modulo = {
        "nome": nome,
        "categoria": categoria,
        "setor": setor,
        "status": status,
        "nivel_importancia": nivel_importancia,
        "consumo_percentual": consumo,
        "capacidade_percentual": capacidade,
        "temperatura": temperatura,
        "pressao": pressao,
        "integridade_percentual": integridade,
        "falha_critica": falha_critica,
        "ultima_manutencao": ultima_manutencao
    }

    dados["modulos"].append(novo_modulo)

    with open("dados_colonia.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    registrar_historico(
        f"Novo registro cadastrado: {nome}"
    )

    print("\nRegistro cadastrado com sucesso!")

def executar_assistente_ia():
    print("\n********* ASSISTENTE IA - NCAS ************")

    encontrou_risco = False

    for modulo in dados["modulos"]:

        if validar_alerta(modulo):

            encontrou_risco = True

            print(f"\nAnalisando módulo: {modulo['nome']}")
            print("Consultando modelo de IA...")

            try:
                analise = consultar_assistente_ia(modulo)

                print("\nResposta estruturada do assistente IA:")

                print(json.dumps(
                    analise,
                    indent=4,
                    ensure_ascii=False
                ))

                registrar_historico(
                    f"IA analisou o módulo {modulo['nome']} - "
                    f"Risco: identificado - "
                    f"Prioridade: {modulo['nivel_importancia']}"
                )

            except Exception as erro:
                print(f"\nErro ao consultar o assistente IA: {erro}")

    if not encontrou_risco:
        print("\nNenhum risco operacional identificado.")

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
    print("[6] Assistente IA")
    print("[7] Cadastrar registro")
    print("[0] Encerrar")
    print("\n")

    opcao = input("Escolha uma opção: ")
    print("Você escolheu a opção: ", opcao)

    if opcao == "1":
        print("Visualização de módulos selecionada.")
        exibir_modulos()
    elif opcao == "2":
        print("Consulta de histórico selecionada.")
        consultar_historico()
    elif opcao == "3":
        analisar_alerta() 
    elif opcao == "4":
        print("Validação lógica selecionada.")
        executar_validacao_logica()
    elif opcao == "5":
        exibir_prompts()
    elif opcao == "6":
        executar_assistente_ia() 
    elif opcao == "7":
        cadastrar_registro()
    elif opcao == "0":
        print("Encerrando o NCAS...")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")