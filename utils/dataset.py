
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import streamlit as st

@st.cache_data
def gerar_dataset():

    np.random.seed(42)
    n = 3000

    renda = np.random.normal(5000, 2000, n).clip(1000, 20000)
    score = np.random.normal(600, 150, n).clip(200, 900)
    dividas = np.random.randint(0, 6, n)
    historico = np.random.choice([0, 1], n, p=[0.3, 0.7])

    classe = []

    for i in range(n):
        if score[i] > 700 and dividas[i] <= 1 and historico[i] == 1:
            classe.append(1)
        elif score[i] < 400 or dividas[i] >= 4:
            classe.append(0)
        else:
            prob = 0.6 if historico[i] == 1 else 0.4
            classe.append(np.random.choice([0, 1], p=[1-prob, prob]))

    df = pd.DataFrame({
        'renda': renda.astype(int),
        'score': score.astype(int),
        'dividas': dividas,
        'historico': historico,
        'classe': classe
    })

    return df


def preparar_dados(df):

    X = df[['renda', 'score', 'dividas', 'historico']]
    y = df['classe']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.3, random_state=42
    )

    return X_train, X_test, y_train, y_test, scaler