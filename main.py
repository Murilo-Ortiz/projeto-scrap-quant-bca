import pandas as pd
from src.bcb_api import coletar_dados_bcb, coletar_multiplos_indicadores
from src.preprocessamento import preprocessar_dados
from src.estatisticas import estatisticas_basicas, media_movel, variacao_percentual
from src.modeloRegressao import regressao_linear
from src.arima import ajustar_arima
import matplotlib.pyplot as plt

# Coletar dados
indicadores = ['4189', '11', '126']
dados = coletar_multiplos_indicadores(indicadores, '2020-01-01', '2024-12-31')

dados_processados = preprocessar_dados(dados)

# Estatísticas básicas
estatisticas = estatisticas_basicas(dados_processados)
print(estatisticas)

# Análise de Tendências
dados_movel = media_movel(dados_processados)
dados_variacao = variacao_percentual(dados_processados)

# Visualizando médias móveis
dados_movel[['selic', 'selic_mm']].plot(title="Média Móvel de Selic")
plt.show()

# Visualizando variação percentual
dados_variacao[['selic', 'ipca']].plot(title="Variação Percentual de Selic e IPCA")
plt.show()

# Aplicar modelo de regressão linear para IPCA vs Selic
regressao_linear(dados_processados)

# Aplicar ARIMA para IPCA (com diferenciação, se necessário)
if not teste_adfuller(dados_processados['ipca']):
    dados_processados['ipca'] = diferenciacao(dados_processados['ipca'])

resultado_arima = ajustar_arima(dados_processados['ipca'], p=1, d=1, q=1)
