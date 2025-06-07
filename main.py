# main.py

# 1. Importações para o agente de linguagem e variáveis de ambiente

from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os


# 2. Importações dos módulos internos do projeto

from agente_inteligente.ler_csv import ler_csvs_notas
from agente_inteligente.filtros import filtrar_por_estado


# 3. Carrega a chave da OpenAI do arquivo .env

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 4. Lê os arquivos CSV (cabecalho e itens)

df_cabecalho, df_itens = ler_csvs_notas()



# 5. Apresenta uma prévia dos dados

print("\n📄 Amostra do cabeçalho original:")
print(df_cabecalho.head())


# 6. Aplica filtro por estado (exemplo: Paraíba - "PB")

uf_escolhida = "PB"
df_filtrado = filtrar_por_estado(df_cabecalho, uf_escolhida)


# 7. Gera pergunta com base nos dados filtrados

quantidade = len(df_filtrado)
mensagem_usuario = (
    f"Foram encontradas {quantidade} notas fiscais emitidas no estado da {uf_escolhida}. "
    "Qual a importância de analisar essas emissões por estado?"
)


# 8. Inicializa o modelo da OpenAI

llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key=api_key,
    temperature=0.3
)


# 9. Envia a pergunta e recebe a resposta

resposta = llm.invoke([HumanMessage(content=mensagem_usuario)])


# 10. Exibe a resposta do agente

print("\n💬 Resposta do agente:")
print(resposta.content)
