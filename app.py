import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

@st.cache
def load_data():
  data = pd.read_csv('dengue_geral.csv')
  data[['cod_mun', 'cod_est']] = data[['cod_mun', 'cod_est']].astype(str)
  data['ano'] = pd.to_datetime(data['ano'], format='%Y').dt.year
  data['num_casos'] = data['num_casos'].astype(int)
  return data

data = load_data()

st.title('Dengue Dashboard')
st.write('Painel de visualização de dados epidemiológicos da dengue no Brasil, nos estados e nos municípios, conforme dados disponibilizados pelo DATASUS.')

st.header('Séries temporais de casos notificados')

st.subheader('Brasil')

total_casos_ano_br = data.groupby(['ano']).num_casos.sum().reset_index()
fig_br = px.line(total_casos_ano_br, x = 'ano', y = 'num_casos')
st.plotly_chart(fig_br)

st.subheader('Por estado')
estados = np.sort(data.estado.unique())

estado = st.selectbox('Selecione um estado', estados)

data_estado = data[data['estado'] == estado]
total_casos_ano_est = data_estado.groupby(['ano']).num_casos.sum().reset_index()

fig_est = px.line(total_casos_ano_est, x = 'ano', y = 'num_casos')
st.plotly_chart(fig_est)

st.subheader('Por município')

estado_mun = st.selectbox('Selecione o estado', estados)

municipios = np.sort(data[data['estado'] == estado_mun].municipio.unique())
municipio = st.selectbox('Selecione o município', municipios)

data_municipio = data[data['municipio'] == municipio]
total_casos_ano_mun = data_municipio.groupby(['ano']).num_casos.sum().reset_index()
fig_mun = px.line(total_casos_ano_mun, x = 'ano', y = 'num_casos')
st.plotly_chart(fig_mun)