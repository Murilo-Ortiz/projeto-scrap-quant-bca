import pandas as pd

def preprocessar_dados(dados_dict: dict, normalizar: bool = False, metodo_norm: str = "minmax") -> pd.DataFrame:
    """
    Recebe um dicionário de DataFrames com colunas ['data', 'valor'] e retorna um único DataFrame unificado por data.

    Args:
        dados_dict (dict): {'selic': df_selic, 'ipca': df_ipca, ...}
        normalizar (bool): Se True, normaliza os dados
        metodo_norm (str): 'minmax' ou 'zscore'

    Returns:
        DataFrame: df unificado com colunas ['data', 'selic', 'ipca', ...]
    """
    dfs = []

    for nome, df in dados_dict.items():
        if df.empty:
            print(f"[!] DataFrame para {nome} está vazio. Ignorando.")
            continue

        df = df.copy()
        df = df[["data", "valor"]]
        df.columns = ["data", nome]
        df["data"] = pd.to_datetime(df["data"])
        dfs.append(df)

    if not dfs:
        print("[!] Nenhum dado válido foi encontrado para o processamento.")
        return pd.DataFrame()  # Retorna um DataFrame vazio caso não haja dados válidos

    # Merge por data
    df_merged = dfs[0]
    for df in dfs[1:]:
        df_merged = pd.merge(df_merged, df, on="data", how="outer")

    # Ordena e define índice
    df_merged = df_merged.sort_values("data")
    df_merged.set_index("data", inplace=True)

    # Tratamento de ausentes
    df_merged = df_merged.ffill().bfill()  # ou apenas ffill() se preferir

    # Normalização opcional
    if normalizar:
        if metodo_norm == "minmax":
            df_merged = (df_merged - df_merged.min()) / (df_merged.max() - df_merged.min())
        elif metodo_norm == "zscore":
            df_merged = (df_merged - df_merged.mean()) / df_merged.std()

    return df_merged
