from src.bcb_api import coletar_multiplos_indicadores
from src.modeloRegressao import regressao_linear_indicadores
from src.estatisticas import estatisticas_basicas, media_movel, variacao_percentual, relacao_indicadores
from src.preprocessamento import preprocessar_dados
from src.arima import teste_adfuller, ajustar_arima
import matplotlib.pyplot as plt

if __name__ == "__main__":
    indicadores = ['selic', 'ipca', 'cambio']
    data_inicio = "2023-01-01"
    data_fim = "2023-12-31"

    # 1. Coleta
    dados = coletar_multiplos_indicadores(indicadores, data_inicio, data_fim)

    # 2. Pré-processamento (sem normalização)
    df_unificado = preprocessar_dados(dados, True)

    if df_unificado.empty:
        print("❌ Falha no pré-processamento: DataFrame unificado está vazio.")
    else:
        print("✅ Dados unificados com sucesso:")
        print(df_unificado.head())

    # Estatísticas básicas
    estat = estatisticas_basicas(df_unificado)
    print("📊 Estatísticas básicas:")
    print(estat)

    # Média móvel (30 dias)
    df_mm = media_movel(df_unificado)
    print("📈 Colunas com médias móveis adicionadas:")
    print(df_mm.head())

    # Variação percentual
    df_var = variacao_percentual(df_unificado)
    print("📉 Variação percentual (diária ou mensal):")
    print(df_var.head())

    # Relação entre indicadores (gráficos de dispersão)
    relacao_indicadores(df_unificado)

    regressao_linear_indicadores(df_unificado, "selic", "ipca")
    regressao_linear_indicadores(df_unificado, "cambio", "ipca")
    regressao_linear_indicadores(df_unificado, "cambio", "selic")

# Teste de estacionariedade e previsão ARIMA para o IPCA
if teste_adfuller(df_unificado["ipca"]):
    modelo_ipca = ajustar_arima(df_unificado["ipca"], p=1, d=0, q=1)
else:
    # Diferencia e aplica o ARIMA com d=1
    serie_diferenciada = df_unificado["ipca"].diff().dropna()
    modelo_ipca = ajustar_arima(serie_diferenciada, p=1, d=1, q=1)
