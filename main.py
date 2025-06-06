# main.py

from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

# Importa a função de leitura dos arquivos CSV
from agente_inteligente.ler_csv import ler_csvs_notas

# 1. Carrega a chave da API
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 2. Lê os arquivos CSV
df_cabecalho, df_itens = ler_csvs_notas()

# 3. Mostra uma amostra dos dados lidos
print("\n📄 Amostra do cabeçalho das notas fiscais:")
print(df_cabecalho.head())

print("\n📦 Amostra dos itens das notas fiscais:")
print(df_itens.head())

# 4. Prepara uma pergunta baseada nos dados
pergunta = f"Quantas notas fiscais foram emitidas no total neste conjunto de dados? O arquivo contém {len(df_cabecalho)} registros."

# 5. Inicializa o modelo
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key=api_key,
    temperature=0.3
)

# 6. Envia a pergunta para o modelo
mensagem = HumanMessage(content=pergunta)
resposta = llm.invoke([mensagem])

# 7. Exibe a resposta
print("\n💬 Resposta do agente:")
print(resposta.content)
