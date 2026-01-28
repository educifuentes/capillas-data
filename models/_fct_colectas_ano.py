import pandas as pd
from models._dim_comunas_censo_2024 import stg_cod_comunas
from utilities.load_sources import load_table_to_dataframe

def stg_colectas_ano():
    # Load sources
    colectas_ano = load_table_to_dataframe('colectas_por_ano')
    raw_comunas = load_table_to_dataframe('Cod_comuna')
    
    # Process comunas
    comunas_df = stg_cod_comunas(raw_comunas)
    
    if colectas_ano is not None and comunas_df is not None:
        # Perform left join
        # Left key: 'cod_comuna', Right key: 'codigo_comuna'
        df_joined = pd.merge(
            colectas_ano, 
            comunas_df, 
            left_on='cod_comuna', 
            right_on='codigo_comuna', 
            how='left'
        )
        return df_joined
    
    return None

if __name__ == "__main__":
    df_fct = stg_colectas_ano()
    if df_fct is not None:
        print("Successfully merged colectas_por_ano with comunas")
        print(df_fct.head())
