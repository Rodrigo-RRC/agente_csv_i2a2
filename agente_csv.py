import os
import zipfile

def descompactar_arquivo(nome_arquivo_zip, pasta_raiz="dados"):
    """
    Recebe o nome de um arquivo ZIP e descompacta na pasta:
    dados/descompactado/NOME_DO_ARQUIVO_SEM_ZIP
    """

    # Caminho completo até o ZIP: dados/202401_NFs.zip
    caminho_completo_zip = os.path.join(pasta_raiz, nome_arquivo_zip)

    # Verifica se o arquivo realmente existe
    if not os.path.exists(caminho_completo_zip):
        print(f"❌ Arquivo '{nome_arquivo_zip}' não encontrado dentro de '{pasta_raiz}/'")
        return None

    # Separa o nome do arquivo da extensão .zip
    nome_base_sem_extensao = os.path.splitext(nome_arquivo_zip)[0]  # Exemplo: "202401_NFs"

    # Define a pasta final de saída, ex: dados/descompactado/202401_NFs
    pasta_destino = os.path.join(pasta_raiz, "descompactado", nome_base_sem_extensao)

    # Cria essa pasta caso ainda não exista
    os.makedirs(pasta_destino, exist_ok=True)

    # Descompacta o arquivo na pasta definida
    with zipfile.ZipFile(caminho_completo_zip, 'r') as zip_ref:
        zip_ref.extractall(pasta_destino)

    # Lista os arquivos que foram extraídos
    arquivos_extraidos = os.listdir(pasta_destino)

    print(f"✅ Arquivo '{nome_arquivo_zip}' descompactado com sucesso!")
    print(f"📂 Arquivos extraídos em '{pasta_destino}':")
    for nome_arquivo in arquivos_extraidos:
        print("   └──", nome_arquivo)

    return pasta_destino
