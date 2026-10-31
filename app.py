import pandas as pd
import plotly.express as px
import streamlit as st
# Lendo o arquivo CSV com os dados dos veículos:
car_data = pd.read_csv('vehicles.csv')  # lendo os dados

st.header('Venda de Carros')  # Título do aplicativo
scatter_checkbox = st.checkbox('gráfico de dispersão')


if scatter_checkbox:
    # escrever uma mensagem
    st.write('Criando um gráfico de dispersão para as colunas odometer e price do dataset de veículos')

    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y='price')

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
