import pandas as pd
import unicodedata

def filtrar_por_estado(df: pd.DataFrame, uf: str, coluna: str = "UF") -> pd.DataFrame:
    """
    Filtra o DataFrame com base no estado (UF) informado.

    Parâmetros:
        df (pd.DataFrame): O DataFrame original com os dados.
        uf (str): A sigla do estado que será usada no filtro, como 'PB' ou 'SP'.
        coluna (str): O nome exato da coluna onde está a UF, como 'UF EMITENTE'.

    Retorna:
        pd.DataFrame: Um novo DataFrame contendo apenas as linhas filtradas.
    """
    if coluna not in df.columns:
        print(f"❌ Coluna '{coluna}' não encontrada no DataFrame.")
        return df

    df_filtrado = df[df[coluna].astype(str).str.strip().str.upper() == uf.strip().upper()]
    print(f"🔎 {len(df_filtrado)} registros encontrados para o estado: {uf}")
    return df_filtrado


def normalizar_texto(texto: str) -> str:
    """
    Remove acentos, converte para maiúsculo e tira espaços extras.
    """
    if not isinstance(texto, str):
        return ""
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')
    return texto.strip().upper()


def filtrar_por_municipio(df: pd.DataFrame, municipio: str, coluna: str = "MUNICÍPIO EMITENTE") -> pd.DataFrame:
    """
    Filtra o DataFrame por município, aceitando variações (acentos, maiúsculas etc.).
    Busca aproximada (contém o texto normalizado).
    """
    if coluna not in df.columns:
        print(f"❌ Coluna '{coluna}' não encontrada no DataFrame.")
        return df

    df[coluna + "_NORMALIZADO"] = df[coluna].apply(normalizar_texto)
    municipio_normalizado = normalizar_texto(municipio)

    df_filtrado = df[df[coluna + "_NORMALIZADO"].str.contains(municipio_normalizado)]

    print(f"🔎 {len(df_filtrado)} registros encontrados para o município: {municipio.upper()}")
    return df_filtrado
