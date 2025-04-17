import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def estatisticas_basicas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula estatísticas básicas para o DataFrame de dados.
    """
    stats = df.describe().T[['mean', 'std']]
    stats['correlacao_selic_ipca'] = df['selic'].corr(df['ipca'])
    stats['correlacao_selic_cambio'] = df['selic'].corr(df['cambio'])
    stats['correlacao_ipca_cambio'] = df['ipca'].corr(df['cambio'])
    return stats

def media_movel(df: pd.DataFrame, window: int = 30) -> pd.DataFrame:
    """
    Calcula a média móvel para cada indicador.
    """
    df_movel = df.copy()
    for col in df.columns:
        df_movel[f'{col}_mm'] = df[col].rolling(window=window).mean()
    return df_movel

def variacao_percentual(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula a variação percentual diária.
    """
    df_variacao = df.pct_change() * 100  # multiplicamos por 100 para ter em %
    return df_variacao

def relacao_indicadores(df: pd.DataFrame) -> None:
    """
    Cria gráficos de dispersão para analisar as relações entre os indicadores.
    """
    plt.figure(figsize=(12, 8))

    # Relacionamento IPCA vs Selic
    plt.subplot(2, 2, 1)
    sns.scatterplot(data=df, x='selic', y='ipca')
    plt.title('IPCA vs Selic')

    # Relacionamento IPCA vs Câmbio
    plt.subplot(2, 2, 2)
    sns.scatterplot(data=df, x='ipca', y='cambio')
    plt.title('IPCA vs Câmbio')

    # Relacionamento Selic vs Câmbio
    plt.subplot(2, 2, 3)
    sns.scatterplot(data=df, x='selic', y='cambio')
    plt.title('Selic vs Câmbio')

    plt.tight_layout()
    plt.show()
