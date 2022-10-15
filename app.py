import streamlit as st
import pandas as pd
import numpy as np

@st.cache
def load_data():
  data = pd.read_csv('dengue_geral.csv')
  return data

data = load_data()

st.title('Dengue Dashboard')
st.write('Painel de visualização de dados epidemiológicos da dengue no Brasil, nos estados e nos municípios, conforme dados disponibilizados pelo DATASUS.')

st.header('Séries temporais de casos notificados')

st.subheader('Brasil')

st.subheader('Por estado')
estados = np.sort(data.estado.unique())

estado = st.selectbox('Selecione um estado', estados)

data_estado = data[data['estado'] == estado]
total_casos = data_estado['num_casos'].sum()

st.write('Você selecionou:', estado,'. Total de casos notificados:', total_casos)
data_estado

st.subheader('Por município')