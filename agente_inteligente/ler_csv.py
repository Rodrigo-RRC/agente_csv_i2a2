import pandas as pd
import os

def ler_csvs_notas(caminho_base="dados/descompactado"):
    """
    Lê os arquivos CSV de cabeçalho e itens das notas fiscais

    Retorna:
        df_cabecalho (DataFrame): Dados de cabeçalho das NFs
        df_itens (DataFrame): Dados dos itens das NFs
    """
    try:
        caminho_cabecalho = os.path.join(caminho_base, "202401_NFs_Cabecalho.csv")
        caminho_itens = os.path.join(caminho_base, "202401_NFs_Itens.csv")

        df_cabecalho = pd.read_csv(caminho_cabecalho, sep=None, engine="python", encoding="utf-8")
        df_itens = pd.read_csv(caminho_itens, sep=None, engine="python", encoding="utf-8")

        print("✅ Arquivos CSV lidos com sucesso.")
        return df_cabecalho, df_itens

    except Exception as e:
        print(f"❌ Erro ao ler arquivos CSV em '{caminho_base}': {e}")
        return None, None
