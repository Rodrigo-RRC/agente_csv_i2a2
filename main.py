# main.py

# Importa o modelo de chat da OpenAI da versão correta (langchain_community)
from langchain_community.chat_models import ChatOpenAI

# Importa a estrutura da mensagem do usuário
from langchain.schema import HumanMessage

# Carrega variáveis de ambiente (como a chave da OpenAI)
from dotenv import load_dotenv
import os

# 1. Carrega o arquivo .env com a chave da API
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 2. Inicializa o modelo GPT-3.5-turbo com chave e temperatura definida
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key=api_key,
    temperature=0.3  # Baixa criatividade, respostas mais objetivas
)

# 3. Cria a mensagem do usuário
mensagem = HumanMessage(content="Explique de forma simples o que é uma nota fiscal.")

# 4. Envia a mensagem ao modelo e obtém a resposta (forma recomendada: .invoke)
resposta = llm.invoke([mensagem])

# 5. Exibe a resposta no terminal
print("\n💬 Resposta do agente:")
print(resposta.content)
