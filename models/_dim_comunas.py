import pandas as pd
import sys
import os

# Ensure we can import from utilities
sys.path.append(os.path.join(os.path.dirname(__file__)))

try:
    from utilities.load_sources import load_table_to_dataframe
except ImportError:
    # Fallback for different execution contexts
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from models.utilities.load_sources import load_table_to_dataframe

def load_dim_comunas():
    """
    Loads specific tables required for dimension comunas.
    """
    # Load specific tables
    df_apxs = load_table_to_dataframe('Data APXS 2017')
    df_cod_comuna = load_table_to_dataframe('Cod_comuna')
    
    return df_apxs, df_cod_comuna

def stg_cod_comunas(df_cod_comuna):
    """
    Renames columns and selects subset.
    """
    if df_cod_comuna is not None:
        # Rename to match requirements
        df_cod_comuna = df_cod_comuna.rename(columns={
            'cod_comuna': 'codigo_comuna',
            'n_region': 'region',
            'n_provincia': 'provincia'
        })
        
        # Select columns - based on actual source columns
        selected_columns = ['codigo_comuna', 'comuna_nombre', 'region', 'provincia']
        df_cod_comuna = df_cod_comuna[selected_columns].copy()
        
        print("Model Output - DIM columnas")
        print("Final df_cod_comuna shape:", df_cod_comuna.shape)
        print(df_cod_comuna.head())
        
    return df_cod_comuna

def transform_dim_comunas(df_cod_comuna, df_apxs):
    """
    Performs a left join with df_cod_comuna on the left and df_apxs on the right.
    """
    if df_cod_comuna is None or df_apxs is None:
        print("Missing DataFrames for join.")
        return None
        
    print("Performing left join on 'codigo_comuna'...")
    # Perform the left join
    df_joined = pd.merge(df_cod_comuna, df_apxs, on='codigo_comuna', how='left')
    
    return df_joined

if __name__ == "__main__":
    df_apxs, df_cod_comuna = load_dim_comunas()
    
    # 1. Clean cod_comuna (Rename and Select)
    df_cod_comuna = clean_cod_comuna(df_cod_comuna)
    
    # 2. Transform (Left Join)
    df_dim_comunas = transform_dim_comunas(df_cod_comuna, df_apxs)
    
    if df_dim_comunas is not None:
        print("Successfully created 'df_dim_comunas' (Left Join result)")
        print(f"Columns in joined DF: {df_dim_comunas.columns.tolist()}")
        print(df_dim_comunas.head())