import sklearn
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np
from statsmodels.tsa.stattools import adfuller

def teste_adfuller(series: pd.Series) -> bool:
    """
    Aplica o teste de Dickey-Fuller para verificar a estacionariedade da série temporal.
    """
    resultado = adfuller(series.dropna())  # Remover NaN antes de aplicar
    p_value = resultado[1]
    if p_value < 0.05:
        print("A série é estacionária (p-value < 0.05).")
        return True
    else:
        print("A série não é estacionária (p-value >= 0.05).")
        return False

def diferenciacao(series: pd.Series) -> pd.Series:
    """
    Aplica diferenciação de ordem 1 para tornar a série estacionária.
    """
    return series.diff().dropna()

def ajustar_arima(series: pd.Series, p: int = 1, d: int = 1, q: int = 1) -> None:
    """
    Ajusta um modelo ARIMA aos dados da série temporal.
    """
    modelo = ARIMA(series, order=(p, d, q))
    resultado = modelo.fit()

    print(resultado.summary())  # Resumo do modelo

    # Previsão
    previsao = resultado.forecast(steps=30)  # Previsão para os próximos 30 dias
    plt.figure(figsize=(10, 6))
    plt.plot(series, label="Dados Reais")
    plt.plot(pd.date_range(series.index[-1], periods=30, freq='D'), previsao, label="Previsão ARIMA", color='red')
    plt.title("Previsão ARIMA")
    plt.legend()
    plt.show()


    return resultado

def avaliar_modelo(modelo, series: pd.Series) -> None:
    """
    Avalia a precisão do modelo ARIMA.
    """
    previsao = modelo.fittedvalues
    mse = mean_squared_error(series[1:], previsao)  # Ignorar o primeiro valor (pois é diferenciado)
    rmse = np.sqrt(mse)
    print(f"RMSE: {rmse:.2f}")
