import requests
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

API_URL = "http://127.0.0.1:8000"

st.title("Mini‑Projeto Integrado em Python")

st.header("📊 Estatísticas")
response = requests.get(f"{API_URL}/stats")

if response.status_code == 200:
    st.json(response.json())
else:
    st.error("Erro ao acessar a API")

st.header("📈 Gráfico de Preço")
df = pd.read_csv("data/dados.csv")

fig, ax = plt.subplots()
ax.hist(df["preco"], bins=5)
ax.set_title("Distribuição de Preços")
ax.set_xlabel("Preço")
ax.set_ylabel("Frequência")
st.pyplot(fig)

st.header("➕ Testar Soma")
x = st.number_input("Valor X", step=1.0)
y = st.number_input("Valor Y", step=1.0)

if st.button("Somar"):
    r = requests.post(f"{API_URL}/soma", json={"x": x, "y": y})
    st.success(f"Resultado: {r.json()['resultado']}")