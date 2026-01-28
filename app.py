import streamlit as st

from utilities.load_sources import load_table_to_dataframe
from models._fct_colectas_unitaria import stg_colectas_unitaria
from models._fct_colectas_ano import stg_colectas_ano

st.title("Capillas")

# sources
colecta_unitaria = load_table_to_dataframe("analisis_COLECTA_unitaria")
cod_comuna = load_table_to_dataframe("Cod_comuna")
colectas_por_ano = load_table_to_dataframe("colectas_por_ano")
comunas_2017 = load_table_to_dataframe("data_apxs_2017")


st.header("Modelos", divider = True)
st.markdown(" joined df - colectas unitarias + cod comunas")


fct_colectas = stg_colectas_unitaria()
st.dataframe(fct_colectas)

st.markdown(" joined df - colectas por ano + cod comunas")
fct_colectas_ano = stg_colectas_ano()
st.dataframe(fct_colectas_ano)


### ---

st.header("Fuentes", divider = True)

st.subheader("colectas unitaria")
st.dataframe(colecta_unitaria)

st.subheader("colectas por ano")
st.dataframe(colectas_por_ano)

st.subheader("cod_comuna")
st.dataframe(cod_comuna)

st.subheader("comunas_2017")
st.dataframe(comunas_2017)

