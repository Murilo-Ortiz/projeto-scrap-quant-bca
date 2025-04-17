import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.stattools import adfuller

# Define pasta de saída
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

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

def diferenciacao(series: pd.Series, nome_serie: str = "serie") -> pd.Series:
    """
    Aplica diferenciação de ordem 1 para tornar a série estacionária.
    Salva um gráfico da série diferenciada.
    """
    serie_diff = series.diff().dropna()

    plt.figure(figsize=(10, 4))
    plt.plot(serie_diff)
    plt.title("Série Diferenciada")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, f"{nome_serie}_diferenciada.png"))
    plt.close()

    return serie_diff

def ajustar_arima(series: pd.Series, p: int = 1, d: int = 1, q: int = 1, nome_serie: str = "serie") -> ARIMA:
    """
    Ajusta um modelo ARIMA aos dados da série temporal.
    Salva gráficos da série original e da previsão.
    """
    plt.figure(figsize=(10, 4))
    plt.plot(series)
    plt.title("Série Original")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, f"{nome_serie}_original.png"))
    plt.close()

    modelo = ARIMA(series, order=(p, d, q))
    resultado = modelo.fit()

    print(resultado.summary())

    # Previsão futura
    previsao = resultado.forecast(steps=30)

    plt.figure(figsize=(10, 4))
    plt.plot(series, label="Histórico")
    plt.plot(pd.date_range(start=series.index[-1], periods=31, freq='D')[1:], previsao, label="Previsão", color="red")
    plt.legend()
    plt.title("Previsão ARIMA")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, f"{nome_serie}_previsao.png"))
    plt.close()

    return resultado

def avaliar_modelo(modelo, series: pd.Series) -> None:
    """
    Avalia a precisão do modelo ARIMA.
    """
    previsao = modelo.fittedvalues
    mse = mean_squared_error(series[1:], previsao)  # Ignorar o primeiro valor (pois é diferenciado)
    rmse = np.sqrt(mse)
    print(f"RMSE: {rmse:.2f}")
