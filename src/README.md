# 📈 Análise Quantitativa de Indicadores Econômicos

Este projeto realiza uma análise quantitativa de séries temporais de indicadores econômicos extraídos da API do Banco Central do Brasil (BCB). O foco está em três áreas principais:

- Estatísticas descritivas básicas
- Modelagem com ARIMA
- Regressão linear simples

---

## 🧠 Estatísticas Básicas

Antes de aplicar qualquer modelo, são calculadas estatísticas básicas das séries temporais:

- **Média (mean)**: Valor médio da série.
- **Desvio padrão (std)**: Mede a variabilidade dos dados.
- **Mínimo e máximo**: Limites inferior e superior da série.
- **Mediana (median)**: Valor central da série ordenada.
- **Coeficiente de variação**: Desvio padrão dividido pela média (em %), útil para comparar variabilidade entre séries de diferentes magnitudes.

Essas estatísticas nos ajudam a entender o comportamento inicial da série e a detectar possíveis anomalias, tendências ou sazonalidades.

---

## 🔁 Modelo ARIMA

### O que é?

ARIMA (AutoRegressive Integrated Moving Average) é um modelo estatístico usado para previsão de séries temporais. Ele combina três componentes:

- **AR (AutoRegressive)**: Componente autorregressivo, que usa a dependência entre valores defasados da série.
- **I (Integrated)**: Parte de diferenciação, usada para tornar séries não estacionárias em estacionárias.
- **MA (Moving Average)**: Componente de média móvel dos resíduos de modelos passados.

### Aplicação

O modelo ARIMA é ajustado automaticamente com parâmetros \( (p, d, q) \), onde:

- \( p \): número de defasagens da série (AR)
- \( d \): número de diferenciações aplicadas para estacionariedade
- \( q \): número de defasagens da média móvel (MA)

Também é feito o **teste de estacionariedade de Dickey-Fuller aumentado (ADF)** para verificar se a série precisa de diferenciação antes da modelagem.

Após o ajuste, o modelo realiza **previsões futuras** (por padrão, 30 passos à frente).

---

## 📉 Regressão Linear Simples

É utilizada para analisar a relação entre dois indicadores econômicos, por exemplo:

- **IPCA vs. Selic**
- **Câmbio vs. Selic**
- etc.

O modelo assume a forma:

\[
Y = a + bX
\]

Onde:

- \( Y \): variável dependente (ex: IPCA)
- \( X \): variável independente (ex: Selic)
- \( a \): intercepto
- \( b \): coeficiente angular (inclinação da reta)

O objetivo é **verificar correlação** e **prever o valor de um indicador com base em outro**.

Também são utilizados:

- **R² (coeficiente de determinação)**: Mede o quão bem a variável independente explica a dependente.
- **Gráficos de dispersão com linha de regressão** para visualização.


---

## ⚠️ Observação

Este projeto tem fins **educacionais** e **exploratórios**. As previsões e análises não devem ser utilizadas para decisões financeiras sem validação rigorosa com especialistas.



