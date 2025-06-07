# filtros.py

#🧾 Função 1: Filtrar por estado (UF)

# Importamos o pandas pois todas as operações de filtragem
# que faremos são com DataFrames, que é a estrutura do pandas.

import pandas as pd


# Esta função recebe um DataFrame (df) e uma UF (ex: "PB").
# Ela retorna apenas as linhas do DataFrame em que a coluna "UF" é igual à UF informada.


def filtrar_por_estado(df: pd.DataFrame, uf: str) -> pd.DataFrame:

"""
    Filtra o DataFrame por unidade federativa (estado).

    Parâmetros:
        df: DataFrame de entrada (ex: df_cabecalho)
        uf: Sigla do estado (ex: "PB", "SP", "RJ")

    Retorna:
        DataFrame contendo apenas as linhas da UF informada.
    """

# Padroniza a UF para maiúsculas, caso o usuário informe em minúsculas
    uf = uf.upper()

# Verifica se a coluna "UF" existe no DataFrame
    if "UF" not in df.columns:
        print("❌ Coluna 'UF' não encontrada no DataFrame.")
        return df

# Filtra o DataFrame onde a coluna "UF" é igual à uf fornecida
    df_filtrado = df[df["UF"] == uf]


# Mostra o número de registros encontrados
    print(f"🔎 {len(df_filtrado)} registros encontrados para o estado: {uf}")
    return df_filtrado


#🏙️ Função 2: Filtrar por município

# Esta função é parecida com a anterior, mas agora o filtro é pela coluna "MUNICIPIO".

def filtrar_por_municipio(df: pd.DataFrame, municipio: str) -> pd.DataFrame:
    """
    Filtra o DataFrame por nome de município (cidade).

    Parâmetros:
        df: DataFrame de entrada (ex: df_cabecalho)
        municipio: Nome da cidade a ser buscada (ex: "João Pessoa")

    Retorna:
        DataFrame contendo apenas as linhas da cidade informada.
    """
    # Padroniza o nome para caixa alta, se necessário
    municipio = municipio.strip().upper()

    # Verifica se a coluna "MUNICIPIO" existe no DataFrame
    if "MUNICIPIO" not in df.columns:
        print("❌ Coluna 'MUNICIPIO' não encontrada no DataFrame.")
        return df

    # Filtra pelas cidades cujo nome, em maiúsculas, bate com o informado
    df_filtrado = df[df["MUNICIPIO"].str.upper() == municipio]

    # Mostra o número de registros encontrados
    print(f"🏙️ {len(df_filtrado)} registros encontrados para o município: {municipio.title()}")
    return df_filtrado

# ✅ Finalização do módulo
# Fim do módulo filtros.py

# Outras funções poderão ser adicionadas aqui no futuro:
# - Filtrar por data
# - Filtrar por CNPJ
# - Agregações por produto ou NCM
