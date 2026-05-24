# components/analise_cliente.py
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px


def render_analise_cliente(knn, p, scaler, X_train, y_train):

    st.markdown("# Análise de Cliente")
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Renda Mensal")
        renda = st.number_input(
            "", min_value=1000.0, max_value=50000.0, value=5000.0, step=500.0
        )
        st.markdown("#### Score de Crédito")
        score = st.slider("", 200, 900, 650)

    with col2:
        st.markdown("#### Quantidade de Dívidas")
        dividas = st.slider(" ", 0, 10, 1)
        st.markdown("#### Histórico de Pagamento")
        historico = st.selectbox(
            " ", [1, 0],
            format_func=lambda x: "Bom" if x == 1 else "Ruim"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Analisar Cliente"):

        novo_cliente = np.array([[renda, score, dividas, historico]])
        novo_cliente_scaled = scaler.transform(novo_cliente)

        res_knn = knn.predict(novo_cliente_scaled)[0]
        res_p = p.predict(novo_cliente_scaled)[0]
        classificacao_final = 1 if (res_knn + res_p) >= 1 else 0

        def traduzir(x):
            return "Bom pagador" if x == 1 else "Alto risco"

        st.markdown("---")

        if classificacao_final == 1:
            st.markdown("""
                <div style="
                    background: linear-gradient(135deg, #064e3b, #065f46);
                    border-left: 5px solid #22c55e;
                    border-radius: 12px;
                    padding: 24px;
                    text-align: center;
                    font-size: 26px;
                    font-weight: bold;
                    color: white;
                    margin-bottom: 20px;
                ">CLIENTE APROVADO</div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div style="
                    background: linear-gradient(135deg, #7f1d1d, #991b1b);
                    border-left: 5px solid #ef4444;
                    border-radius: 12px;
                    padding: 24px;
                    text-align: center;
                    font-size: 26px;
                    font-weight: bold;
                    color: white;
                    margin-bottom: 20px;
                ">CLIENTE DE ALTO RISCO</div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### Resultado dos Modelos")
        c1, c2 = st.columns(2)
        c1.metric("KNN", traduzir(res_knn))
        c2.metric("Perceptron", traduzir(res_p))

        def recomendar_credito(renda, score, dividas, classificacao):
            if classificacao == 1:
                if score > 700 and dividas == 0:
                    return renda * 0.5
                elif score > 600:
                    return renda * 0.3
                else:
                    return renda * 0.2
            else:
                if score < 400 or dividas >= 4:
                    return 0
                else:
                    return renda * 0.1

        credito = recomendar_credito(renda, score, dividas, classificacao_final)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### Crédito Recomendado")
        st.markdown(f"""
            <div style="
                background-color: #1e293b;
                border-left: 4px solid #6366f1;
                border-radius: 10px;
                padding: 16px 24px;
                font-size: 22px;
                font-weight: bold;
                color: white;
            ">R$ {credito:,.2f}</div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### Nível de Risco")
        if score >= 700:
            risco_cor = "#22c55e"
            risco_texto = "Baixo Risco"
        elif score >= 500:
            risco_cor = "#f59e0b"
            risco_texto = "Risco Moderado"
        else:
            risco_cor = "#ef4444"
            risco_texto = "Alto Risco"

        st.markdown(f"""
            <div style="
                background-color: #1e293b;
                border-left: 4px solid {risco_cor};
                border-radius: 10px;
                padding: 14px 24px;
                font-size: 18px;
                color: white;
            ">{risco_texto}</div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### Explicação do Modelo")
        explicacoes = []
        if score > 700:
            explicacoes.append(("check-circle", "#22c55e", "Score elevado"))
        if dividas <= 1:
            explicacoes.append(("check-circle", "#22c55e", "Poucas dívidas"))
        if historico == 1:
            explicacoes.append(("check-circle", "#22c55e", "Histórico financeiro positivo"))
        if renda > 7000:
            explicacoes.append(("check-circle", "#22c55e", "Boa capacidade financeira"))
        if score < 500:
            explicacoes.append(("exclamation-triangle", "#f59e0b", "Score abaixo do recomendado"))
        if dividas >= 4:
            explicacoes.append(("exclamation-triangle", "#f59e0b", "Muitas dívidas registradas"))

        for icone, cor, texto in explicacoes:
            st.markdown(f"""
                <div style="
                    background-color: #1e293b;
                    border-left: 3px solid {cor};
                    border-radius: 8px;
                    padding: 10px 16px;
                    margin-bottom: 8px;
                    color: white;
                ">
                    <i class="bi bi-{icone}" style="color:{cor}; margin-right:8px;"></i>{texto}
                </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### Cliente e Vizinhos Mais Próximos")

        distancias = np.linalg.norm(X_train - novo_cliente_scaled, axis=1)
        indices = np.argsort(distancias)[:5]
        X_plot = X_train[:, :2]
        cliente_plot = novo_cliente_scaled[:, :2]

        fig_knn = px.scatter(
            x=X_plot[:, 0],
            y=X_plot[:, 1],
            color=y_train.astype(str),
            color_discrete_map={"0": "#ef4444", "1": "#6366f1"},
            opacity=0.4,
            template="plotly_dark",
            labels={"x": "Renda Normalizada", "y": "Score Normalizado", "color": "Classe"},
        )
        fig_knn.add_scatter(
            x=X_plot[indices, 0],
            y=X_plot[indices, 1],
            mode="markers",
            marker=dict(size=14, color="#a855f7", symbol="square",
                        line=dict(width=2, color="white")),
            name="Vizinhos"
        )
        fig_knn.add_scatter(
            x=cliente_plot[:, 0],
            y=cliente_plot[:, 1],
            mode="markers",
            marker=dict(size=18, color="#f59e0b", symbol="star",
                        line=dict(width=2, color="white")),
            name="Cliente"
        )
        fig_knn.update_layout(
            paper_bgcolor="#0f172a",
            plot_bgcolor="#1e293b",
            margin=dict(l=20, r=20, t=20, b=20),
            legend=dict(bgcolor="#1e293b", bordercolor="#334155", borderwidth=1),
        )
        st.plotly_chart(fig_knn, use_container_width=True)

        st.markdown("### Clientes Mais Próximos")
        dados_vizinhos = []
        for i in indices:
            original = scaler.inverse_transform([X_train[i]])[0]
            dados_vizinhos.append({
                "Renda": int(original[0]),
                "Score": int(original[1]),
                "Dívidas": int(original[2]),
                "Histórico": "Bom" if original[3] == 1 else "Ruim",
                "Classe": "Bom pagador" if y_train.iloc[i] == 1 else "Alto risco"
            })
        st.dataframe(pd.DataFrame(dados_vizinhos), use_container_width=True)