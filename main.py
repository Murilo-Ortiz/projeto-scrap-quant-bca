from src.bcb_api import coletar_multiplos_indicadores

# Baixa e salva SELIC, IPCA e dólar
dados = coletar_multiplos_indicadores(
    indicadores=["selic", "ipca", "cambio"],
    data_inicial="01/01/2015",
    data_final="31/12/2024",
    salvar_csv=True
)

# Acessa um DataFrame específico
df_selic = dados["selic"]
print(df_selic.head())
