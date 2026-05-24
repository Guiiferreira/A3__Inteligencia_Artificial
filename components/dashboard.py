
import streamlit as st
import plotly.express as px


def render_dashboard(df, acc_knn, acc_p):

    st.markdown("# Agente Inteligente de Análise de Crédito")
    st.markdown("---")
    st.markdown("## Dashboard Geral")
    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Clientes", len(df))
    col2.metric("Acurácia KNN", f"{acc_knn:.2%}")
    col3.metric("Acurácia Perceptron", f"{acc_p:.2%}")
    col4.metric("Média Score", int(df['score'].mean()))

    st.markdown("---")

    colA, colB = st.columns(2)

    with colA:
        st.markdown("#### Distribuição do Score")
        fig1 = px.histogram(
            df, x="score",
            nbins=30,
            color_discrete_sequence=["#6366f1"],
            template="plotly_dark",
        )
        fig1.update_layout(
            paper_bgcolor="#0f172a",
            plot_bgcolor="#1e293b",
            margin=dict(l=20, r=20, t=20, b=20),
            showlegend=False,
            xaxis=dict(title="Score", color="#94a3b8"),
            yaxis=dict(title="Frequência", color="#94a3b8"),
        )
        fig1.update_traces(marker_line_width=0)
        st.plotly_chart(fig1, use_container_width=True)

    with colB:
        st.markdown("#### Distribuição de Classes")
        fig2 = px.bar(
            x=["Alto Risco", "Bom Pagador"],
            y=df["classe"].value_counts().values,
            color=["Alto Risco", "Bom Pagador"],
            color_discrete_map={"Alto Risco": "#a855f7", "Bom Pagador": "#6366f1"},
            template="plotly_dark",
        )
        fig2.update_layout(
            paper_bgcolor="#0f172a",
            plot_bgcolor="#1e293b",
            margin=dict(l=20, r=20, t=20, b=20),
            showlegend=False,
            xaxis=dict(color="#94a3b8"),
            yaxis=dict(title="Quantidade", color="#94a3b8"),
        )
        fig2.update_traces(marker_line_width=0)
        st.plotly_chart(fig2, use_container_width=True)