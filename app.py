import streamlit as st

from utilities.load_sources import load_table_to_dataframe

st.title("Capillas")

# sources
colecta_unitaria = load_table_to_dataframe("analisis_COLECTA_unitaria")
comunas = load_table_to_dataframe("Cod_comuna")
colectas_por_ano = load_table_to_dataframe("colectas_por_ano")

st.subheader("sources")

st.markdown("### colectas")
st.dataframe(colecta_unitaria)

st.markdown("### comunas")
st.dataframe(comunas)

st.markdown("### colectas por ano")
st.dataframe(colectas_por_ano)
