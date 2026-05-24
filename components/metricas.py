# components/metricas.py
import streamlit as st
import plotly.express as px
from sklearn.metrics import confusion_matrix


def render_metricas(y_test, y_pred_knn, y_pred_p, acc_knn, acc_p):

    st.markdown("# Avaliação dos Modelos")
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Matriz de Confusão - KNN")
        cm_knn = confusion_matrix(y_test, y_pred_knn)
        fig_knn = px.imshow(
            cm_knn,
            text_auto=True,
            color_continuous_scale="Purples",
            template="plotly_dark",
            x=["Alto Risco", "Bom Pagador"],
            y=["Alto Risco", "Bom Pagador"],
        )
        fig_knn.update_layout(
            paper_bgcolor="#0f172a",
            plot_bgcolor="#1e293b",
            margin=dict(l=20, r=20, t=20, b=20),
            xaxis=dict(title="Previsto", color="#94a3b8"),
            yaxis=dict(title="Real", color="#94a3b8"),
            coloraxis_showscale=False,
        )
        st.plotly_chart(fig_knn, use_container_width=True)

    with col2:
        st.markdown("#### Matriz de Confusão - Perceptron")
        cm_p = confusion_matrix(y_test, y_pred_p)
        fig_p = px.imshow(
            cm_p,
            text_auto=True,
            color_continuous_scale="Purples",
            template="plotly_dark",
            x=["Alto Risco", "Bom Pagador"],
            y=["Alto Risco", "Bom Pagador"],
        )
        fig_p.update_layout(
            paper_bgcolor="#0f172a",
            plot_bgcolor="#1e293b",
            margin=dict(l=20, r=20, t=20, b=20),
            xaxis=dict(title="Previsto", color="#94a3b8"),
            yaxis=dict(title="Real", color="#94a3b8"),
            coloraxis_showscale=False,
        )
        st.plotly_chart(fig_p, use_container_width=True)

    st.markdown("---")
    st.markdown("#### Comparação de Acurácia")
    fig3 = px.bar(
        x=["KNN", "Perceptron"],
        y=[acc_knn, acc_p],
        color=["KNN", "Perceptron"],
        color_discrete_map={"KNN": "#6366f1", "Perceptron": "#a855f7"},
        template="plotly_dark",
        text=[f"{acc_knn:.2%}", f"{acc_p:.2%}"],
    )
    fig3.update_layout(
        paper_bgcolor="#0f172a",
        plot_bgcolor="#1e293b",
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=False,
        yaxis=dict(tickformat=".0%", color="#94a3b8"),
        xaxis=dict(color="#94a3b8"),
    )
    fig3.update_traces(marker_line_width=0, textfont_color="white", textposition="outside")
    st.plotly_chart(fig3, use_container_width=True)