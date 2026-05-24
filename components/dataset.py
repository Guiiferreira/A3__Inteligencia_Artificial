# components/dataset.py
import streamlit as st


def render_dataset(df):

    st.markdown("# Visualização do Dataset")
    st.markdown("---")

    st.dataframe(df, use_container_width=True)

    st.markdown("### Estatísticas")
    st.dataframe(df.describe(), use_container_width=True)

    st.markdown("---")

    st.download_button(
        label="Baixar Dataset CSV",
        data=df.to_csv(index=False),
        file_name="dataset_credito.csv",
        mime="text/csv"
    )