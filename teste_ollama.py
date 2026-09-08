from ollama import chat

resposta = chat(
    model="qwen3:4b",
    messages=[
        {
            "role": "user",
            "content": "Explique em uma frase o que é uma inteligência artificial."
        }
    ]
)

print(resposta.message.content)