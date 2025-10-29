````markdown
# 🧠 Hello World AI + LangChain — Práctica Resumen

**Estudiante:** Manuel Barrera  
**Curso:** IA en el Aula — Nivel Avanzado  
**Profesor:** Luis Daniel Benavides Navarro  
**Fecha:** Octubre 2025  

---

## 🚀 Descripción

En esta práctica se configuró un entorno en **VS Code** con **Python**, **Jupyter Notebook** y la **API de OpenAI**.  
Se realizaron ejemplos básicos de generación de texto y se introdujo **LangChain** para crear cadenas de prompts.

---

## ⚙️ Configuración

1. Crear carpeta del proyecto y entorno virtual:
   ```bash
   python -m venv .venv
````

2. Activar el entorno y abrirlo en VS Code.
3. Instalar dependencias:

   ```bash
   pip install openai python-dotenv langchain langchain-openai jupyter
   ```
4. Crear archivo `.env`:

   ```
   OPENAI_API_KEY=tu_clave_aqui
   ```
5. Añadir a `.gitignore`:

   ```
   .env
   venv/
   ```

---

## 💬 Ejemplo 1 — Hello World con OpenAI

```python
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = "Escribe un saludo tipo 'Hello World' con un toque creativo de IA."
resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.6
)
print(resp.choices[0].message.content)
```

✅ **Resultado:** el modelo genera un saludo creativo de IA.
Se probó con distintos valores de `temperature` y `max_tokens`.

---

## 🔗 Ejemplo 2 — Uso básico de LangChain

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
prompt = ChatPromptTemplate.from_template("Explica brevemente el concepto de {tema}.")
chain = prompt | llm | StrOutputParser()

print(chain.invoke({"tema": "aprendizaje automático"}))
```

✅ **Resultado:** el modelo explica el concepto de forma breve y coherente.

---

## 🔁 Ejemplo 3 — Cadena secuencial

```python
from langchain.chains import SimpleSequentialChain, LLMChain
from langchain.prompts import PromptTemplate

primer_prompt = PromptTemplate(
    input_variables=["tema"],
    template="Explica brevemente el concepto de {tema}."
)
segundo_prompt = PromptTemplate(
    input_variables=["concepto"],
    template="Propón una aplicación educativa del siguiente concepto: {concepto}."
)

primer_chain = LLMChain(llm=llm, prompt=primer_prompt)
segundo_chain = LLMChain(llm=llm, prompt=segundo_prompt)
chain_secuencial = SimpleSequentialChain(chains=[primer_chain, segundo_chain])

print(chain_secuencial.run("realidad aumentada"))
```

✅ **Resultado:** el modelo explica el concepto y propone una aplicación educativa.

---

## 🧠 Conclusión

* Se configuró correctamente el entorno de IA con **Python y OpenAI**.
* Se realizaron pruebas de generación de texto desde un **notebook**.
* Se aprendió el uso básico de **LangChain** para crear cadenas de prompts.
