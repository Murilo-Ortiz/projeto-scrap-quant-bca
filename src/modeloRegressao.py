import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def regressao_linear_indicadores(df: pd.DataFrame, x_col: str, y_col: str) -> None:
    """
    Aplica uma regressão linear simples para prever um indicador com base em outro.

    Args:
        df (pd.DataFrame): DataFrame com os dados.
        x_col (str): Nome da coluna preditora (variável independente).
        y_col (str): Nome da coluna alvo (variável dependente).
    """
    # Remove ausentes nas colunas escolhidas
    dados = df[[x_col, y_col]].dropna()

    X = dados[[x_col]]
    y = dados[y_col]

    modelo = LinearRegression()
    modelo.fit(X, y)
    y_pred = modelo.predict(X)

    # Gráfico
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, label="Dados Reais", color="blue")
    plt.plot(X, y_pred, label="Previsão (Regressão Linear)", color="red")
    plt.title(f"Regressão Linear: {y_col} vs {x_col}")
    plt.xlabel(x_col.capitalize())
    plt.ylabel(y_col.capitalize())
    plt.legend()
    plt.tight_layout()
    plt.show()

    print(f"Coeficiente de determinação (R²): {modelo.score(X, y):.4f}")
    print(f"Intercepto: {modelo.intercept_:.4f}")
    print(f"Coeficiente (slope): {modelo.coef_[0]:.4f}")
