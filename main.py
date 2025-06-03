# main.py
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

# 1. Carrega a chave da OpenAI do .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 2. Inicializa o modelo GPT-3.5 com temperatura baixa
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key=api_key,
    temperature=0.3
)

# 3. Criar a mensagem que o usuário deseja fazer ao agente
mensagem = HumanMessage(content="Explique de forma simples o que é uma nota fiscal.")

# 4. Enviar a mensagem para o modelo e receber resposta
resposta = llm([mensagem])

# 5. Mostrar a resposta no terminal
print("\n💬 Resposta do agente:")
print(resposta.content)
