# NCAS — Núcleo Cognitivo da Aurora Siger

Protótipo acadêmico desenvolvido em Python para registro, organização, consulta e interpretação de dados operacionais de uma colônia espacial fictícia.

## Sobre o projeto

O **Núcleo Cognitivo da Aurora Siger (NCAS)** simula uma central operacional capaz de:

- carregar dados estruturados em JSON;
- cadastrar novos módulos da colônia;
- persistir alterações no arquivo JSON;
- registrar eventos em arquivo TXT;
- consultar os registros salvos;
- identificar riscos por meio de regras booleanas;
- apresentar a lógica utilizada na tomada de decisão;
- trabalhar com Zero-Shot, Few-Shot e Structured Output;
- consultar um modelo de linguagem local;
- transformar a análise da IA em uma resposta estruturada.

O objetivo é integrar, em um único protótipo, conceitos de **Python, arquivos, JSON, lógica booleana, engenharia de prompts e Inteligência Artificial**.

---

## Arquitetura

```text
                 ┌─────────────────────┐
                 │      Usuário        │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Menu do NCAS     │
                 └──────────┬──────────┘
                            │
              ┌─────────────┼──────────────┐
              ▼             ▼              ▼
          Cadastro       Consulta       Validação
              │             │              │
              ▼             ▼              ▼
        dados_colonia   registros_      Regra
           .json        colonia.txt     booleana
              │                            │
              └──────────────┬─────────────┘
                             ▼
                    ┌─────────────────┐
                    │ Ollama / Qwen3  │
                    │      :4b        │
                    └────────┬────────┘
                             ▼
                    Análise estruturada
```

## Tecnologias

- **Python**
- **JSON**
- **TXT**
- **Ollama**
- **Qwen3:4B**
- **Git / GitHub**

### Principais recursos Python utilizados

- `open()`
- `with`
- modos de arquivo `r`, `w` e `a`
- `read()` / operações de escrita
- dicionários e listas
- `json.load()`
- `json.dump()`
- funções
- condicionais
- operadores booleanos
- tratamento de exceções

---

## Como executar

### 1. Pré-requisitos

Instale:

- Python 3.x
- Ollama

Depois, confirme:

```bash
python --version
ollama --version
```

### 2. Baixar o modelo

```bash
ollama pull qwen3:4b
```

Verifique:

```bash
ollama list
```

### 3. Criar e ativar o ambiente virtual

Windows / Git Bash:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

### 4. Instalar a biblioteca Python

```bash
pip install ollama
```

### 5. Executar

```bash
python codigo_fonte.py
```

---

## Menu

O sistema disponibiliza operações como:

```text
[1] Visualizar módulos
[2] Consultar histórico
[3] Analisar alertas
[4] Executar validação lógica
[5] Exibir prompts
[6] Assistente IA
[7] Cadastrar registro
[0] Encerrar
```

### Cadastro

A opção de cadastro cria um novo dicionário com os dados do módulo e o adiciona à lista `modulos`.

Depois, o sistema salva novamente o JSON utilizando:

```python
json.dump(dados, arquivo, indent=4, ensure_ascii=False)
```

---

## Regra de decisão

A regra principal utilizada pelo NCAS é:

```text
RISCO = F OR A OR I
```

Onde:

```text
F = falha crítica
A = status de alerta
I = integridade abaixo de 80%
```

Em Python:

```python
risco = falha_critica or status_alerta or integridade_baixa
```

Portanto, basta uma das condições ser verdadeira para o módulo ser classificado como risco.

### Exemplo

```text
Falha crítica: False
Status alerta: True
Integridade baixa: False

Resultado: True
```

O módulo é considerado de risco porque seu status está em alerta.

---

## Simplificação booleana

Uma forma equivalente de demonstrar a simplificação é:

```text
R = (F AND C) OR (F AND NOT C) OR A OR I

R = F AND (C OR NOT C) OR A OR I

R = F AND True OR A OR I

R = F OR A OR I
```

A expressão final é exatamente a utilizada pelo programa.

---

## Inteligência Artificial

O NCAS utiliza **Ollama** para executar localmente o modelo **Qwen3:4B**.

A aplicação Python envia ao modelo:

- nome do módulo;
- categoria;
- setor;
- status;
- nível de importância;
- consumo;
- capacidade;
- temperatura;
- pressão;
- integridade;
- falha crítica;
- resultado da validação lógica.

O prompt orienta o modelo a retornar uma estrutura semelhante a:

```json
{
  "modulo": "",
  "prioridade": "",
  "risco": "",
  "resumo": "",
  "recomendacao": "",
  "acao_humana": ""
}
```

### Por que a validação é feita antes da IA?

A regra de negócio fica sob controle determinístico do programa.

```text
Dados
  ↓
Python
  ↓
Regra lógica
  ↓
Risco identificado
  ↓
IA interpreta e recomenda
```

Assim, a IA atua como uma camada de interpretação e recomendação, não como a única responsável pela decisão operacional. Essa escolha foi pensada também sob a perspectiva do uso responsável e ético da Inteligência Artificial, evitando que decisões potencialmente críticas sejam delegadas integralmente ao modelo. Dessa forma, as regras lógicas e as validações realizadas pelo sistema permanecem como uma camada determinística de controle, enquanto a IA complementa o processo com interpretação e recomendações. Isso permite aproveitar os recursos da Inteligência Artificial sem retirar a responsabilidade humana sobre decisões que possam impactar a operação da colônia.

---

## Engenharia de prompts

O projeto demonstra três abordagens:

### Zero-Shot

A tarefa é apresentada diretamente, sem exemplos.

### Few-Shot

Um ou mais exemplos são fornecidos para orientar o comportamento esperado.

### Structured Output

O modelo recebe uma estrutura de resposta definida, facilitando o processamento pelo programa.

---

## Estrutura de dados

Exemplo simplificado:

```json
{
  "modulos": [
    {
      "nome": "Sistema de Oxigenio",
      "categoria": "Suporte Vital",
      "setor": "Operacional",
      "status": "ativo",
      "nivel_importancia": "critico",
      "consumo_percentual": 82,
      "capacidade_percentual": 95,
      "temperatura": 22,
      "pressao": 101,
      "integridade_percentual": 96,
      "falha_critica": false,
      "ultima_manutencao": "..."
    }
  ],
  "alertas": []
}
```

---

## Arquivos do projeto

```text
NCAS/
├── codigo_fonte.py
├── dados_colonia.json
├── registros_colonia.txt
├── regras_logicas.pdf
├── prompts_utilizados.pdf
├── link_video.txt
└── README.md
```
---

## Contexto acadêmico

Projeto desenvolvido para aplicação prática dos conceitos de:

- manipulação de arquivos;
- JSON;
- dicionários e listas;
- lógica booleana;
- LLMs;
- engenharia de prompts;
- memória e armazenamento;
- otimização de modelos;
- responsabilidade e uso ético de Inteligência Artificial.

---

## Status

**Projeto acadêmico — protótipo funcional.**

A implementação pode ser expandida futuramente com:

- validação mais robusta dos dados de entrada;
- edição e remoção de módulos;
- filtros de consulta;
- autenticação;
- interface web;
- banco de dados;
- testes automatizados;
- observabilidade;
- integração com outros modelos locais ou APIs.

---

## Para rodar: python codigo_fonte.py
//

## Autor

```bash
Integrantes
Nome: ANA CAROLINA FREIRE MAFRA – rm573650
Nome: Daniel Guimarães Barreto – rm573425
Nome: Paulo Henrique da Silva Gola – rm572992
Nome: Vinicius Daniel de Borba – rm572091
Nome: Vitor de Araujo Ferreira – rm572838

---

Projeto desenvolvido para fins acadêmicos.
