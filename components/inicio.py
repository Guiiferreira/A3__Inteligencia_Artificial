# components/inicio.py
import streamlit as st
import pandas as pd


def render_inicio():

    st.markdown("# Agente Inteligente de Análise de Crédito")
    st.markdown("---")

    # Descrição
    st.markdown("""
        <div style="
            background-color: #1e293b;
            border-left: 4px solid #6366f1;
            border-radius: 10px;
            padding: 20px 24px;
            margin-bottom: 20px;
            color: white;
            font-size: 16px;
            line-height: 1.7;
        ">
            Este projeto tem como objetivo desenvolver um agente inteligente para análise de crédito,
            utilizando técnicas de Machine Learning, especificamente os algoritmos KNN (K-Nearest Neighbors)
            e Perceptron.<br><br>
            O sistema simula um cenário real de instituições financeiras, sendo capaz de:
            <ul style="color:#94a3b8; margin-top:10px; margin-bottom:10px;">
                <li>Classificar clientes como bons pagadores ou de alto risco</li>
                <li>Recomendar limites de crédito com base no perfil financeiro</li>
                <li>Avaliar solicitações de aumento de crédito</li>
            </ul>
            Para isso, foi utilizado um dataset sintético contendo informações como renda, score de crédito,
            quantidade de dívidas e histórico financeiro.<br><br>
            Além da aplicação dos modelos, o projeto também integra regras de negócio, permitindo que as
            decisões tomadas sejam interpretáveis e próximas de situações reais do mercado.<br><br>
            Dessa forma, o sistema não se limita à classificação, atuando como um agente de apoio à tomada
            de decisão em concessão de crédito.
        </div>
    """, unsafe_allow_html=True)

    # Modelos
    st.markdown("### Modelos Utilizados")

    # KNN
    st.markdown("""
        <div style="
            background-color: #1e293b;
            border-left: 4px solid #6366f1;
            border-radius: 10px;
            padding: 20px 24px;
            margin-bottom: 12px;
            color: white;
            font-size: 15px;
            line-height: 1.8;
        ">
            <div style="font-size:17px; font-weight:600; margin-bottom:10px; color:#a5b4fc;">
                KNN (K-Nearest Neighbors)
            </div>
            <div style="color:#94a3b8; margin-bottom:6px;">
                <i class="bi bi-diamond-fill" style="color:#6366f1; margin-right:8px;"></i>Baseado em similaridade entre clientes
            </div>
            <div style="color:#94a3b8; margin-bottom:6px;">
                <i class="bi bi-diamond-fill" style="color:#6366f1; margin-right:8px;"></i>Utiliza distância para classificação
            </div>
            <div style="color:#94a3b8;">
                <i class="bi bi-diamond-fill" style="color:#6366f1; margin-right:8px;"></i>Interpretável através dos vizinhos mais próximos
            </div>
        </div>
    """, unsafe_allow_html=True)

   # Perceptron
    st.markdown("""
        <div style="
            background-color: #1e293b;
            border-left: 4px solid #a855f7;
            border-radius: 10px;
            padding: 20px 24px;
            margin-bottom: 20px;
            color: white;
            font-size: 15px;
            line-height: 1.8;
        ">
            <div style="font-size:17px; font-weight:600; margin-bottom:10px; color:#d8b4fe;">
                Perceptron
            </div>
            <div style="color:#94a3b8; margin-bottom:6px;">
                <i class="bi bi-diamond-fill" style="color:#a855f7; margin-right:8px;"></i>Modelo linear
            </div>
            <div style="color:#94a3b8; margin-bottom:6px;">
                <i class="bi bi-diamond-fill" style="color:#a855f7; margin-right:8px;"></i>Aprende uma fronteira de decisão
            </div>
            <div style="color:#94a3b8;">
                <i class="bi bi-diamond-fill" style="color:#a855f7; margin-right:8px;"></i>Mais rápido e generalista
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Funcionalidades
    st.markdown("### Funcionalidades")

    funcionalidades = [
        "Classificação de clientes (Bom pagador / Alto risco)",
        "Comparação entre dois modelos (KNN e Perceptron)",
        "Recomendação de crédito baseada no perfil",
        "Avaliação de aumento de limite",
        "Visualização dos dados e decisões",
        "Explicação do modelo KNN (vizinhos mais próximos)",
    ]

    for f in funcionalidades:
        st.markdown(f"""
            <div style="
                background-color: #1e293b;
                border-left: 3px solid #22c55e;
                border-radius: 8px;
                padding: 10px 16px;
                margin-bottom: 8px;
                color: white;
            ">
                <i class="bi bi-check-circle" style="color:#22c55e; margin-right:8px;"></i>{f}
            </div>
        """, unsafe_allow_html=True)

    # Integrantes
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Integrantes")

    integrantes = [
        ("Guilherme Loula Teixeira",              "823144030"),
        ("Guilherme Pereira Nascimento Ferreira",  "823122900"),
        ("Leandro Moises Vaz",                     "823150188"),
        ("Murilo Sabino F. De Melo",               "824114526"),
        ("Taissa Almeida Souza De Jesus",          "823144189"),
        ("Victor Hugo Luz Rodrigues Barbosa",      "824147318"),
    ]

    df_integrantes = pd.DataFrame(integrantes, columns=["Nome", "RA"])
    st.dataframe(df_integrantes, use_container_width=True, hide_index=True)