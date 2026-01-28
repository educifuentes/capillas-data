import streamlit as st

from utilities.load_sources import load_table_to_dataframe
from models._fct_colectas_unitaria import stg_colectas_unitaria
from models._fct_colectas_ano import stg_colectas_ano
from models._dim_comunas_2017 import stg_comunas_2017

st.title("Capillas")

# sources
colecta_unitaria = load_table_to_dataframe("analisis_COLECTA_unitaria")
cod_comuna = load_table_to_dataframe("Cod_comuna")
colectas_por_ano = load_table_to_dataframe("colectas_por_ano")
comunas_2017 = load_table_to_dataframe("data_apxs_2017")


st.header("Finales", divider = True)
st.markdown(" joined df - colectas unitarias + cod comunas 2024 + comunas 2017")


fct_colectas = stg_colectas_unitaria()
st.dataframe(fct_colectas)

st.markdown(" joined df - colectas por ano + cod comunas")
fct_colectas_ano = stg_colectas_ano()
st.dataframe(fct_colectas_ano)

st.header("Intermediate", divider = True)

st.markdown("stg comunas 2017 - se hizo reshape")
stg_comunas_2017 = stg_comunas_2017()
st.dataframe(stg_comunas_2017)

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

