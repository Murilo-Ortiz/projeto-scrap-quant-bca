task_md = """
# 📋 Projeto: Análise Quantitativa com Indicadores Econômicos do Banco Central

Este é o backlog de tarefas para desenvolvimento do projeto, seguindo uma estrutura baseada em metodologias ágeis (Scrum/Kanban). As tarefas estão organizadas por etapas.

---

## 🧠 Planejamento
- [x] Montar estrutura de pastas do projeto
- [x] Criar ambiente virtual com `venv`
- [x] Inicializar repositório Git
- [ ] Definir objetivo principal do projeto (ex: impacto da Selic e IPCA em ativos financeiros)
- [ ] Escolher os indicadores econômicos a serem utilizados
- [ ] Listar códigos das séries temporais no SGS/BCB

---

## 📥 Coleta de Dados
- [ ] Criar função para coletar dados da API do BCB (`src/bcb_api.py`)
- [ ] Adicionar suporte para múltiplos indicadores simultaneamente
- [ ] Salvar dados coletados em arquivos CSV (`/data`)
- [ ] Permitir seleção de intervalo de datas na coleta
- [ ] Validar respostas da API (tratamento de erro)

---

## 🧹 Processamento de Dados
- [ ] Padronizar formato de datas e números
- [ ] Tratar dados ausentes ou inconsistentes
- [ ] Unificar diversas séries em um único DataFrame
- [ ] Criar função de limpeza/normalização dos dados

---

## 📊 Análise Quantitativa
- [ ] Calcular estatísticas básicas (média, desvio padrão, correlação)
- [ ] Analisar tendências (média móvel, variação percentual)
- [ ] Estudar relações entre os indicadores (ex: IPCA vs Selic)
- [ ] Aplicar modelo preditivo simples (ex: regressão linear, ARIMA)

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
"""

# Salvar em arquivo
with open("TASKS.md", "w", encoding="utf-8") as f:
    f.write(task_md)

