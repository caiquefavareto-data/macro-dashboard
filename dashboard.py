import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px

# 1. Configuração da página
st.set_page_config(page_title="Dashboard Macroeconómico", layout="wide")

# 2. Cabeçalho e Descrição
st.title("📊 Painel Analítico Macroeconómico")
st.markdown("Monitorização interativa de indicadores globais: Petróleo e Inflação.")
st.divider()

# 3. Função para extrair os dados do mercado (Petróleo Brent)
@st.cache_data
def carregar_dados_petroleo():
    petroleo = yf.Ticker("BZ=F")
    historico = petroleo.history(period="1y")
    historico.reset_index(inplace=True)
    historico['Date'] = historico['Date'].dt.date
    return historico

# 4. Extração dos Dados de Câmbio (Dólar/Real)
@st.cache_data
def carregar_dados_cambio():
    cambio = yf.Ticker("BRL=X")
    hist_cambio = cambio.history(period="1y")
    hist_cambio.reset_index(inplace=True)
    hist_cambio['Date'] = hist_cambio['Date'].dt.date
    return hist_cambio

# 5. Executando as funções e Unindo as Tabelas (Merge)
dados = carregar_dados_petroleo()
dados_cambio = carregar_dados_cambio()

dados_completos = pd.merge(
    dados[['Date', 'Close']], 
    dados_cambio[['Date', 'Close']], 
    on='Date', 
    suffixes=('_Petroleo', '_Dolar')
)

# ==========================================
# 6. ORGANIZAÇÃO DA INTERFACE EM ABAS (TABS)
# ==========================================

# Criamos as abas de navegação
aba1, aba2 = st.tabs(["🛢️ Análise de Petróleo", "🔗 Correlação e Câmbio"])

# Conteúdo da Primeira Aba
with aba1:
    st.subheader("Extração de Dados Brutos: Barril de Petróleo Brent")
    st.dataframe(dados[['Date', 'Close']].tail(), use_container_width=True)
    
    st.divider()
    st.subheader("📈 Tendência Histórica")
    grafico_petroleo = px.line(dados, x='Date', y='Close', title='Cotação Diária - Petróleo Brent (Último Ano)')
    grafico_petroleo.update_layout(xaxis_title="Data", yaxis_title="Preço (USD)")
    st.plotly_chart(grafico_petroleo, use_container_width=True)

# Conteúdo da Segunda Aba
with aba2:
    st.subheader("🔗 Análise de Correlação: Petróleo Brent vs. Dólar (BRL)")
    
    # Métrica de Correlação
    correlacao = dados_completos['Close_Petroleo'].corr(dados_completos['Close_Dolar'])
    st.metric(label="Índice de Correlação (Pearson)", value=f"{correlacao:.2f}")
    st.write("*Nota: Valores próximos de 1 indicam forte correlação positiva, e próximos de -1 indicam forte correlação negativa.*")
    
    # Gráfico de Dispersão
    grafico_correlacao = px.scatter(
        dados_completos, 
        x='Close_Petroleo', 
        y='Close_Dolar', 
        title='Dispersão: Preço do Petróleo vs. Taxa de Câmbio',
        labels={'Close_Petroleo': 'Preço do Petróleo (USD)', 'Close_Dolar': 'Cotação do Dólar (R$)'},
        opacity=0.7,
        trendline="ols"
    )
    st.plotly_chart(grafico_correlacao, use_container_width=True)