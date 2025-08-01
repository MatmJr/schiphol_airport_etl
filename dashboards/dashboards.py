import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

  
st.title("Dashboard de Voos - Modelos de Avião")

df = pd.read_csv("datasets/transformed_flights.csv")

# Lógica feita na segunda aula
modelos_freq = df["modeloAviao"].value_counts().reset_index()
modelos_freq.columns = ["Modelo de Avião", "Frequência"]
modelos_disponiveis = modelos_freq["Modelo de Avião"].tolist()
selecionados = st.multiselect("Selecione os modelos de avião.", modelos_disponiveis, default=modelos_disponiveis[:5])

# Filtrar dados com base na seleção
modelos_filtrados = modelos_freq[modelos_freq["Modelo de Avião"].isin(selecionados)]
st.subheader("Tabela de Frequência dos Modelos Selecionados")
st.dataframe(modelos_filtrados)
  
# Gráfico
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(modelos_filtrados["Modelo de Avião"], modelos_filtrados["Frequência"], color='orange')
ax.set_title("Modelos de Avião Mais Utilizados")
ax.set_xlabel("Modelo de Avião")
ax.set_ylabel("Frequência")
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)
