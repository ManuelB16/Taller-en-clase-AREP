from openai import OpenAI


prompt = "Escribe un saludo tipo 'Hello World' con un toque creativo de IA."
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.6
)

print("Respuesta del modelo:")
print(response.choices[0].message.content)
