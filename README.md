# A3_UC_Inteligencia_Artificial

---

## 👥 Integrantes

| Nome                                   | RA        | Unidade            | Período  |
|----------------------------------------|-----------|--------------------|----------|
| Guilherme Loula Teixeira               | 823144030 | USJT Paulista      | Noturno  |
| Guilherme Pereira Nascimento Ferreira  | 823122900 | USJT Paulista      | Noturno  |
| Leandro Moises Vaz                     | 823150188 | USJT Paulista      | Noturno  |
| Murilo Sabino F. De Melo               | 824114526 | USJT Paulista      | Noturno  |
| Taissa Almeida Souza De Jesus          | 823144189 | USJT Paulista      | Noturno  |
| Victor Hugo Luz Rodrigues Barbosa      | 824147318 | USJT Paulista      | Noturno  |

---

# Agente Inteligente de Análise de Crédito

## Descrição

Este projeto implementa um agente inteligente para análise de crédito utilizando técnicas de Machine Learning. O sistema é capaz de classificar clientes, recomendar limites de crédito e avaliar solicitações de aumento de limite.

O objetivo é simular um cenário real de tomada de decisão em instituições financeiras, integrando modelos preditivos com regras de negócio.

---
## 🎥 Demonstração

![Demo](demo.gif)

## 🧠 Tecnologias Utilizadas

| Tecnologia | Descrição |
|------------|-----------|
| Python 3.x | Linguagem principal do projeto |
| Streamlit | Framework para interface web interativa |
| NumPy | Cálculos numéricos e manipulação de arrays |
| Pandas | Manipulação e análise de dados |
| Scikit-learn | Modelos de Machine Learning e métricas |
| Plotly | Visualização de dados interativa |
| Bootstrap Icons | Ícones da interface |

---

## 📁 Estrutura do Projeto

```
PROJETO_CREDITO/
│
├── app.py                  # Arquivo principal
├── style.css               # Estilos da interface
│
├── components/             # Páginas da aplicação
│   ├── __init__.py
│   ├── sidebar.py          # Menu de navegação
│   ├── inicio.py           # Página inicial
│   ├── dashboard.py        # Dashboard geral
│   ├── analise_cliente.py  # Análise de cliente
│   ├── metricas.py         # Métricas dos modelos
│   └── dataset.py          # Visualização do dataset
│
└── utils/                  # Utilitários
    ├── __init__.py
    ├── modelos.py          # KNN e Perceptron
    └── dataset.py          # Geração e preparação dos dados
```

---

## ⚙️ Funcionalidades

✔️ Classificação de clientes (Bom pagador / Alto risco)  
✔️ Comparação entre dois modelos (KNN e Perceptron)  
✔️ Recomendação de crédito baseada no perfil  
✔️ Avaliação de aumento de limite  
✔️ Visualização dos dados e decisões  
✔️ Explicação do modelo KNN (vizinhos mais próximos)  

---

## 📊 Modelos Utilizados

### 🔹 KNN (K-Nearest Neighbors)
- Baseado em similaridade entre clientes
- Utiliza distância para classificação
- Interpretável através dos vizinhos mais próximos

---

### 🔹 Perceptron
- Modelo linear
- Aprende uma fronteira de decisão
- Mais rápido e generalista

---

## ▶️ Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

2. Instale as dependências:
```bash
pip install streamlit numpy pandas scikit-learn plotly streamlit-option-menu
```

3. Execute a aplicação:
```bash
python -m streamlit run app.py
```

---

## 🧪 Simulação

O sistema permite inserir dados de um novo cliente:

- Renda mensal
- Score de crédito
- Quantidade de dívidas
- Histórico de pagamento

E retorna:

- Classificação (KNN e Perceptron)
- Recomendação de crédito
- Nível de risco
- Explicação do modelo
- Visualização dos vizinhos mais próximos (KNN)

---

## 📈 Métricas Avaliadas

- Acurácia
- Matriz de confusão
- Comparação entre modelos

---

## 🎯 Objetivo Acadêmico

Este projeto foi desenvolvido com foco educacional, com o objetivo de aplicar conceitos de:

- Machine Learning
- Classificação supervisionada
- Análise de dados
- Desenvolvimento de interfaces web com Streamlit
- Integração com regras de negócio

---

## Diferencial

O projeto vai além da classificação tradicional, simulando decisões reais de concessão de crédito com uma interface web interativa, tornando o modelo mais próximo de aplicações do mercado financeiro.

---

## 📝 Conclusão

Este projeto teve como objetivo desenvolver um sistema inteligente de apoio à análise de crédito, utilizando técnicas de aprendizado supervisionado para classificar clientes quanto ao risco de inadimplência. Foram aplicados dois modelos distintos, o KNN e o Perceptron, permitindo não apenas a previsão do comportamento do cliente, mas também a comparação entre abordagens baseadas em similaridade e em separação linear.

A análise dos resultados demonstrou que diferentes modelos podem apresentar comportamentos distintos diante dos mesmos dados, evidenciando a importância da escolha adequada da técnica e das métricas de avaliação, especialmente em contextos sensíveis como o financeiro. Nesse sentido, foi priorizada a métrica de precisão, visando reduzir o risco de concessão de crédito a clientes inadimplentes.

Como evolução do sistema, foram implementadas funcionalidades adicionais, como a recomendação de valores de crédito e a análise de aumento de limite, aproximando a solução de cenários reais utilizados por instituições financeiras. Essas funcionalidades demonstram como a Inteligência Artificial pode ser integrada a regras de negócio para apoiar a tomada de decisão.

Por fim, conclui-se que o uso de modelos de Machine Learning pode contribuir significativamente para a automação e melhoria dos processos de análise de crédito, tornando as decisões mais rápidas, consistentes e baseadas em dados.

---

👨‍💻 **Autor Principal**  
Guilherme Pereira Nascimento Ferreira  
Engenharia de Software
