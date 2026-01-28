import streamlit as st

from utilities.load_sources import load_table_to_dataframe
from models._fct_colectas_unitaria import stg_colectas_unitaria
from models._fct_colectas_ano import stg_colectas_ano
from models._dim_comunas_2017 import stg_comunas_2017

st.title("Parroquias y Capillas")

# sources
colecta_unitaria = load_table_to_dataframe("analisis_COLECTA_unitaria")
cod_comuna = load_table_to_dataframe("Cod_comuna")
colectas_por_ano = load_table_to_dataframe("colectas_por_ano")
comunas_2017 = load_table_to_dataframe("data_apxs_2017")


st.header("Finales", divider = True)
st.badge("fct_colectas_unitaria")
st.markdown(" Joined df - colectas unitarias + cod comunas 2024 + comunas 2017")


fct_colectas_unitaria = stg_colectas_unitaria()
st.dataframe(fct_colectas_unitaria)

# ---

st.badge("fct_colectas_ano")
st.markdown(" joined df - colectas por ano + cod comunas + comunas 2017")

fct_colectas_ano = stg_colectas_ano()
st.dataframe(fct_colectas_ano)

st.header("Intermediate", divider = True)

st.badge("stg comunas 2017", color="orange")
st.markdown("se hizo reshape")
stg_comunas_2017 = stg_comunas_2017()
st.dataframe(stg_comunas_2017)

### ---

st.header("Fuentes", divider = True)

st.badge("colectas unitaria", color="green")
st.dataframe(colecta_unitaria)

st.badge("colectas por ano", color="green")
st.dataframe(colectas_por_ano)

st.badge("cod_comuna", color="green")
st.dataframe(cod_comuna)

st.badge("comunas_2017", color="green")
st.dataframe(comunas_2017)

