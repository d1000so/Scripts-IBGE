import requests
import pandas as pd

def fetch_and_save(url, keys, file_name):
    """
    Função genérica para buscar dados de uma API, extrair colunas e salvar em CSV.
    
    :param url: URL da API.
    :param keys: Dicionário {nome_coluna: caminho_dados} para extrair os dados.
    :param file_name: Nome do arquivo CSV para salvar os dados.
    :return: DataFrame contendo os dados.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        data = response.json()
        
        # Montar DataFrame a partir das chaves especificadas
        df = pd.DataFrame({col: [eval(f"d{path}") for d in data] for col, path in keys.items()})
        df.to_csv(file_name, index=False, decimal=',', encoding='latin-1')
        print(f"Dados salvos em {file_name}")
        return df
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")
        return pd.DataFrame()

# Funções específicas
def municipio():
    return fetch_and_save(
        url="https://servicodados.ibge.gov.br/api/v1/localidades/municipios",
        keys={
            'Id': "['id']",
            'Município': "['nome']",
            'Id Microrregião': "['microrregiao']['id']"
        },
        file_name="dmunicipio.csv"
    )

def microrregiao():
    return fetch_and_save(
        url="https://servicodados.ibge.gov.br/api/v1/localidades/microrregioes",
        keys={
            'Id': "['id']",
            'Microrregião': "['nome']",
            'Id Mesorregião': "['mesorregiao']['id']"
        },
        file_name="dmicrorregiao.csv"
    )

def mesorregiao():
    return fetch_and_save(
        url="https://servicodados.ibge.gov.br/api/v1/localidades/mesorregioes",
        keys={
            'Id': "['id']",
            'Mesorregião': "['nome']",
            'Id UF': "['UF']['id']"
        },
        file_name="dmesorregiao.csv"
    )

def uf():
    return fetch_and_save(
        url="https://servicodados.ibge.gov.br/api/v1/localidades/estados",
        keys={
            'Id': "['id']",
            'UF': "['nome']",
            'Id Regiao': "['regiao']['id']"
        },
        file_name="dUF.csv"
    )

def regiao():
    return fetch_and_save(
        url="https://servicodados.ibge.gov.br/api/v1/localidades/regioes",
        keys={
            'Id': "['id']",
            'Região': "['nome']"
        },
        file_name="dregiao.csv"
    )

# Exemplo de uso
if __name__ == "__main__":
    municipio()
    microrregiao()
    mesorregiao()
    uf()
    regiao()
