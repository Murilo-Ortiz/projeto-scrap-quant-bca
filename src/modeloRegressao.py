import sklearn 
import pandas as pd
from sklearn.linear_model import LinearRegression

def regressao_linear(df: pd.DataFrame) -> None:
    """
    Aplica uma regressão linear simples para prever o IPCA com base na Selic.
    """
    # Definindo variáveis dependente e independente
    X = df[['selic']].dropna()  # variável independente (Selic)
    y = df['ipca'].dropna()  # variável dependente (IPCA)

    # Ajustando o modelo
    modelo = LinearRegression()
    modelo.fit(X, y)

    # Previsões
    y_pred = modelo.predict(X)

    # Gráfico
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, label="Dados Reais", color="blue")
    plt.plot(X, y_pred, label="Previsão (Regressão Linear)", color="red")
    plt.title("Regressão Linear: IPCA vs Selic")
    plt.xlabel("Selic")
    plt.ylabel("IPCA")
    plt.legend()
    plt.show()

    print(f"Coeficiente de determinação (R²): {modelo.score(X, y)}")
