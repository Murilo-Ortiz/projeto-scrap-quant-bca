# 📊 Análise Quantitativa com Indicadores Econômicos do Banco Central

Este projeto tem como objetivo **analisar a relação entre indicadores econômicos divulgados pelo Banco Central do Brasil** — como a taxa Selic, a inflação medida pelo IPCA e a cotação do dólar comercial (USD/BRL) — e sua **influência sobre o comportamento de ativos financeiros**, visando extrair padrões que possam embasar **estratégias quantitativas de investimento**.

A aplicação realiza a **coleta automatizada de dados via API do SGS/BCB**, com **tratamento e unificação dos dados**, além de **visualizações gráficas** e **análises estatísticas**, incluindo **cálculos de correlação** entre os indicadores e **modelos preditivos simples**, como **regressão linear** e **ARIMA**, para prever possíveis comportamentos futuros.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.x**
- **API SGS do Banco Central do Brasil** - Para coleta de dados econômicos históricos
- **Pandas** - Para manipulação e análise de dados
- **Requests** - Para fazer requisições HTTP à API
- **Matplotlib / Seaborn** - Para visualização gráfica
- **Jupyter Notebook** - Para desenvolvimento interativo e testes
- **Git / GitHub** - Controle de versão e colaboração

---

## ✅ Indicadores Selecionados

O projeto coleta e analisa os seguintes indicadores econômicos:

1. **Selic**  
   Taxa básica de juros anual (% a.a.), usada como referência para as demais taxas de juros da economia.

2. **IPCA (Índice de Preços ao Consumidor Amplo)**  
   Índice utilizado para medir a inflação oficial do Brasil.

3. **Câmbio (USD/BRL)**  
   Cotação do dólar comercial, que pode influenciar o mercado financeiro e ser um fator importante em decisões de investimento.

---

## 📊 Funcionalidades

- **Coleta automatizada de dados**: Os dados são coletados diretamente da API do Banco Central, garantindo informações atualizadas.
- **Tratamento de dados**: O projeto realiza o tratamento dos dados, incluindo a conversão de formatos, preenchimento de valores ausentes e unificação de múltiplas séries temporais em um único DataFrame.
- **Análises estatísticas**: Cálculo de estatísticas básicas, como **média**, **desvio padrão**, e **correlação** entre os indicadores econômicos.
- **Análise de tendências**: Cálculos de **média móvel** e **variação percentual** para identificar possíveis tendências nos dados.
- **Modelos preditivos simples**: Implementação de modelos como **regressão linear** e **ARIMA** para prever o comportamento de um indicador com base em outros.

---

## 🔧 Como Usar

### 1. Clonando o repositório

Primeiro, faça o clone do repositório:

```bash
git clone https://github.com/username/quant.git
cd quant
```

### 2. Instalando dependências
Crie um ambiente virtual e instale as dependências necessárias:

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```
### 3. Utilizando as funcionalidades 
Você pode utilizar as funcionalidades presentes em src/ para fazer as análises estatísticas simples ou análises mais complexas como ARIMA. Faça um teste executando o arquivo main.py 


--- 

## Estrutura do Projeto

```bash
├── README.md             # Documentação do projeto
├── TASKS.md              # Lista de tarefas e próximos passos
├── data                  # Dados coletados (CSV)
│   ├── cambio.csv        # Dados de Câmbio
│   ├── ipca.csv          # Dados de IPCA
│   └── selic.csv         # Dados de Selic
├── main.py               # Script principal
├── notebooks             # Notebooks Jupyter com análises exploratórias
├── requirements.txt      # Dependências do projeto
├── src                   # Código-fonte
│   ├── __init__.py       # Pacote para organização
│   ├── bcb_api.py        # Coleta de dados da API do Banco Central
│   ├── estatisticas.py   # Funções para cálculo de estatísticas
│   ├── modeloRegressao.py# Modelos de regressão e predição
│   ├── preprocessamento.py # Funções de limpeza e preparação dos dados
│   └── arima.py          # Implementação do modelo ARIMA
├── tests                 # Testes automatizados
```
---

### 🛠️ Próximos Passos
Veja a lista de tarefas no arquivo TASKS.md para acompanhar o progresso e as funcionalidades planejadas para o futuro.

---
Sinta-se à vontade para contribuir com o projeto realizando um pull request! Caso deseje, entre em contato por muriloschrortiz@gmail.com 