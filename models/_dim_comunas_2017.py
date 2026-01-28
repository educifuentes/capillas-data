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



def stg_comunas_2017():
    """
    Reshapes comunas_2017 from long to wide format.
    """
    comunas_2017 = load_table_to_dataframe("data_apxs_2017")

    selected_columns = ['codigo_comuna', 'ano', 'Attribute', 'Value']
    comunas_2017 = comunas_2017[selected_columns].copy()

    if comunas_2017 is not None:
        print("STG MODEL COMUNAS 2017 - Reshaping from long to wide")
        
        # Reshape: Long to Wide
        # Index: codigo_comuna, Columns: Attribute comun, Values: Value
        try:
            comunas_wide = comunas_2017.pivot(
                index='codigo_comuna', 
                columns='Attribute', 
                values='Value'
            ).reset_index()
            
            # Clean up: remove index name if present
            comunas_wide.columns.name = None
            
            print("Final df_dim_comunas_2017 shape:", comunas_wide.shape)
            print(comunas_wide.head())
            return comunas_wide
        except Exception as e:
            print(f"Error reshaping comunas_2017: {e}")
            return comunas_2017
        
    return None
