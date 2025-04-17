import os
import pandas as pd
import requests
from datetime import datetime

INDICADORES = {
    "selic": {
        "nome": "Selic diária acumulada",
        "codigo": 11
    },
    "ipca": {
        "nome": "IPCA - Índice Nacional de Preços ao Consumidor Amplo (mensal)",
        "codigo": 433
    },
    "cambio": {
        "nome": "Dólar comercial - venda (fechamento)",
        "codigo": 1
    }
}

def formatar_data(data: str) -> str:
    try:
        return datetime.strptime(data, "%Y-%m-%d").strftime("%d/%m/%Y")
    except ValueError:
        return data  # Se já estiver no formato correto


def coletar_dados_bcb(codigo_serie: int, data_inicial: str = "01/01/2000", data_final: str = None) -> pd.DataFrame:
    if data_final is None:
        data_final = datetime.today().strftime('%d/%m/%Y')

    # Converte datas de 'YYYY-MM-DD' para 'DD/MM/YYYY' se necessário
    try:
        data_inicial = datetime.strptime(data_inicial, "%Y-%m-%d").strftime("%d/%m/%Y")
    except ValueError:
        pass
    try:
        data_final = datetime.strptime(data_final, "%Y-%m-%d").strftime("%d/%m/%Y")
    except ValueError:
        pass

    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados"
    params = {
        "formato": "json",
        "dataInicial": data_inicial,
        "dataFinal": data_final
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        dados = response.json()

        if not dados:
            print(f"[!] Nenhum dado retornado para a série {codigo_serie} ({data_inicial} a {data_final})")
            return pd.DataFrame(columns=["data", "valor"])

        df = pd.DataFrame(dados)
        df['data'] = pd.to_datetime(df['data'], dayfirst=True)
        df['valor'] = df['valor'].str.replace(',', '.').astype(float)

        return df

    except requests.exceptions.HTTPError as err:
        print(f"[Erro HTTP] {err}")
        print(f"URL usada: {response.url}")
    except Exception as e:
        print(f"[Erro] Falha ao coletar dados da série {codigo_serie}: {e}")

    return pd.DataFrame(columns=["data", "valor"])

def coletar_multiplos_indicadores(indicadores: list, data_inicial: str, data_final: str, salvar_csv: bool = False, overwrite_csv: bool = False) -> dict:
    """
    Coleta várias séries do BCB e retorna um dicionário de DataFrames.
    
    Args:
        indicadores (list): Lista de chaves do dicionário INDICADORES (ex: ['selic', 'ipca'])
        data_inicial (str): Data inicial no formato 'DD/MM/YYYY' ou 'YYYY-MM-DD'
        data_final (str): Data final no mesmo formato
        salvar_csv (bool): Se True, salva em /data/nome.csv
        overwrite_csv (bool): Se True, sobrescreve o arquivo CSV se ele já existir
    
    Returns:
        dict: {'selic': df_selic, 'ipca': df_ipca, ...}
    """
    resultados = {}

    for chave in indicadores:
        if chave not in INDICADORES:
            print(f"[!] Indicador '{chave}' não encontrado. Ignorando.")
            continue

        nome = INDICADORES[chave]["nome"]
        codigo = INDICADORES[chave]["codigo"]

        print(f"🔄 Coletando: {nome} ({codigo})")
        df = coletar_dados_bcb(codigo, data_inicial, data_final)
        resultados[chave] = df

        if salvar_csv and not df.empty:
            os.makedirs("data", exist_ok=True)
            caminho = f"data/{chave}.csv"

            if os.path.exists(caminho) and not overwrite_csv:
                print(f"[!] Arquivo {caminho} já existe. Não foi sobrescrito.")
            else:
                df.to_csv(caminho, index=False)
                print(f"✅ Salvo em {caminho}")

    return resultados

