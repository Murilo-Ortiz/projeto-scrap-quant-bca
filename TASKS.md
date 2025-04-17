# 📋 Projeto: Análise Quantitativa com Indicadores Econômicos do Banco Central

Este é o backlog de tarefas para desenvolvimento do projeto, seguindo uma estrutura baseada em metodologias ágeis (Scrum/Kanban). As tarefas estão organizadas por etapas.

---

## 🧠 Planejamento
- [x] Montar estrutura de pastas do projeto
- [x] Criar ambiente virtual com `venv`
- [x] Inicializar repositório Git
- [x] Definir objetivo principal do projeto: "Analisar a relação entre indicadores econômicos divulgados pelo Banco Central do Brasil — como a taxa Selic, inflação (IPCA) e câmbio — e sua influência sobre o comportamento de ativos financeiros, visando extrair padrões que possam embasar estratégias quantitativas de investimento."
- [x] Escolher os indicadores econômicos a serem utilizados

---

## 📥 Coleta de Dados
- [x] Criar função para coletar dados da API do BCB (`src/bcb_api.py`)
- [x] Adicionar suporte para múltiplos indicadores simultaneamente
- [x] Salvar dados coletados em arquivos CSV (`/data`)
- [x] Permitir seleção de intervalo de datas na coleta
- [x] Validar respostas da API (tratamento de erro)

---

## 🧹 Processamento de Dados
- [x] Padronizar formato de datas e números
- [x] Tratar dados ausentes ou inconsistentes
- [x] Unificar diversas séries em um único DataFrame
- [x] Criar função de limpeza/normalização dos dados

---

## 📊 Análise Quantitativa
- [x] Calcular estatísticas básicas (média, desvio padrão, correlação)
- [x] Analisar tendências (média móvel, variação percentual)
- [x] Estudar relações entre os indicadores (ex: IPCA vs Selic)
- [x] Aplicar modelo preditivo simples (ex: regressão linear, ARIMA)

---

## 📈 Visualização
- [ ] Gerar gráfico de linhas (comparando séries ao longo do tempo)
- [ ] Visualizar correlação entre os indicadores
- [ ] Criar visualizações exploratórias com `matplotlib` ou `seaborn`
- [ ] (Opcional) Criar dashboard interativo com `Streamlit` ou `Dash`

---

## 📄 Documentação e Entrega
- [ ] Preencher `README.md` com:
  - Descrição do projeto
  - Instruções de uso
  - Exemplos de visualização
- [ ] Comentar os scripts principais (`main.py`, `bcb_api.py`)
- [ ] Criar notebook exploratório (`/notebooks`)
- [ ] Subir repositório para o GitHub
- [ ] (Opcional) Adicionar testes simples para a função de coleta
