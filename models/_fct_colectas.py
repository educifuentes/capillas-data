from models._dim_comunas import stg_cod_comunas




def stg_colectas():
        colectas_unitaria = load_table_to_dataframe('analisis_COLECTA_unitaria')
        comunas_df = stg_cod_comunas()
 

