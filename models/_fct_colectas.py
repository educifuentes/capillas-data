import pandas as pd
from models._dim_comunas import stg_cod_comunas
from utilities.load_sources import load_table_to_dataframe

def stg_colectas():
    # Load sources
    colectas_unitaria = load_table_to_dataframe('analisis_COLECTA_unitaria')
    raw_comunas = load_table_to_dataframe('Cod_comuna')
    
    # Process comunas
    comunas_df = stg_cod_comunas(raw_comunas)
    
    if colectas_unitaria is not None and comunas_df is not None:
        # Perform left join
        # Left key: 'colectas_unitaria', Right key: 'codigo_comuna'
        df_joined = pd.merge(
            colectas_unitaria, 
            comunas_df, 
            left_on='CodComuna', 
            right_on='codigo_comuna', 
            how='left'
        )
        return df_joined
    
    return None

if __name__ == "__main__":
    df_fct = stg_colectas()
    if df_fct is not None:
        print("Successfully merged colectas with comunas")
        print(df_fct.head())
