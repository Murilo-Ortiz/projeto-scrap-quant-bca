# src/bcb_api.py

import requests
import pandas as pd
from datetime import datetime

INDICADORES = {
    "selic": {
        "nome": "Selic diária acumulada",
        "codigo": 11
    },
    "ipca": {
        "nome": "IPCA - Índice de Preços ao Consumidor Amplo (mensal)",
        "codigo": 433
    },
    "cambio": {
        "nome": "Dólar comercial - venda (fechamento)",
        "codigo": 1
    }
}


def coletar_dados_bcb(codigo_serie: int, data_inicial: str = "2000-01-01", data_final: str = None) -> pd.DataFrame:
    from urllib.parse import quote

    if data_final is None:
        data_final = datetime.today().strftime('%Y-%m-%d')

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
            print(f"[!] Nenhum dado retornado para série {codigo_serie}. Verifique o período: {data_inicial} a {data_final}")
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

import os

def coletar_multiplos_indicadores(indicadores: list, data_inicial: str, data_final: str, salvar_csv: bool = False) -> dict:
    """
    Coleta várias séries do BCB e retorna um dicionário de DataFrames.

    Args:
        indicadores (list): Lista de chaves do dicionário INDICADORES (ex: ['selic', 'ipca'])
        data_inicial (str): Data inicial no formato DD/MM/YYYY
        data_final (str): Data final no formato DD/MM/YYYY
        salvar_csv (bool): Se True, salva cada série em data/<indicador>.csv

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

        print(f"Coletando: {nome} ({codigo})")
        df = coletar_dados_bcb(codigo, data_inicial, data_final)
        resultados[chave] = df

        if salvar_csv:
            os.makedirs("data", exist_ok=True)
            df.to_csv(f"data/{chave}.csv", index=False)
            print(f"[✓] Dados salvos em data/{chave}.csv")

    return resultados