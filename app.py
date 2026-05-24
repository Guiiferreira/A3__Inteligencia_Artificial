# app.py
import streamlit as st

from utils.dataset import gerar_dataset, preparar_dados
from utils.modelos import treinar_modelos
from components.sidebar import render_sidebar
from components.inicio import render_inicio
from components.dashboard import render_dashboard
from components.analise_cliente import render_analise_cliente
from components.metricas import render_metricas
from components.dataset import render_dataset

# ======================================
# CONFIGURAÇÃO DA PÁGINA
# ======================================
st.set_page_config(
    page_title="Agente Inteligente de Crédito",
    layout="wide"
)

# ======================================
# ESTILO
# ======================================
def carregar_css(nome_arquivo):
    with open(nome_arquivo) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

carregar_css("style.css")

st.markdown("""
<link rel="stylesheet"
href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap-icons.css">
""", unsafe_allow_html=True)

# ======================================
# DADOS E MODELOS
# ======================================
df = gerar_dataset()
X_train, X_test, y_train, y_test, scaler = preparar_dados(df)
knn, p, y_pred_knn, y_pred_p, acc_knn, acc_p = treinar_modelos(
    X_train, X_test, y_train, y_test
)

# ======================================
# NAVEGAÇÃO
# ======================================
pagina = render_sidebar()

# ======================================
# PÁGINAS
# ======================================
if pagina == "Início":
    render_inicio()

elif pagina == "Dashboard":
    render_dashboard(df, acc_knn, acc_p)

elif pagina == "Análise de Cliente":
    render_analise_cliente(knn, p, scaler, X_train, y_train)

elif pagina == "Métricas":
    render_metricas(y_test, y_pred_knn, y_pred_p, acc_knn, acc_p)

elif pagina == "Dataset":
    render_dataset(df)

# ======================================
# RODAPÉ
# ======================================
st.markdown("---")
st.markdown("""
    <div style="
        text-align: center;
        padding: 10px;
        color: #94a3b8;
        font-size: 14px;
    ">
        Projeto A3 para UC de Inteligência Artificial
    </div>
""", unsafe_allow_html=True)