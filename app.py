import streamlit as st

from utilities.load_sources import load_table_to_dataframe
from models._fct_colectas import stg_colectas

st.title("Capillas")

# sources
colecta_unitaria = load_table_to_dataframe("analisis_COLECTA_unitaria")
comunas = load_table_to_dataframe("Cod_comuna")
colectas_por_ano = load_table_to_dataframe("colectas_por_ano")


st.header("Modelos", divider = True)


fct_colectas = stg_colectas()
st.dataframe(fct_colectas)


### ---

st.header("Fuentes", divider = True)

st.subheader("colectas")
st.dataframe(colecta_unitaria)

st.subheader("comunas")
st.dataframe(comunas)

st.subheader("colectas por ano")
st.dataframe(colectas_por_ano)
