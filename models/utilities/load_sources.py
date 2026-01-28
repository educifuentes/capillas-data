import yaml
import pandas as pd

def get_source_config(yaml_path='_src_capillas.yml'):
    """
    Reads the sources from a YAML file and returns a list of dictionaries
    for each table with name, url, and sheet_name.
    """
    with open(yaml_path, 'r') as file:
        config = yaml.safe_load(file)
    
    table_configs = []
    for source in config.get('sources', []):
        for table in source.get('tables', []):
            name = table.get('name')
            url = table.get('url')
            sheet_name = table.get('sheet_name')
            
            if name and url:
                table_configs.append({
                    'name': name,
                    'url': url,
                    'sheet_name': sheet_name
                })
    return table_configs

def _prepare_gsheet_url(url):
    """
    Converts a Google Sheets URL to an Excel export link.
    """
    if 'docs.google.com/spreadsheets' in url:
        if '/edit' in url:
            url = url.split('/edit')[0] + '/export?format=xlsx'
        elif not url.endswith('/export?format=xlsx'):
            url = url.rstrip('/') + '/export?format=xlsx'
    return url

def load_table_to_dataframe(table_name, yaml_path='_src_capillas.yml'):
    """
    Loads a specific table defined in the YAML into a pandas DataFrame.
    """
    configs = get_source_config(yaml_path)
    # Find the config for the requested table
    cfg = next((c for c in configs if c['name'] == table_name), None)
    
    if cfg is None:
        print(f"Table '{table_name}' not found in {yaml_path}.")
        return None
        
    url = _prepare_gsheet_url(cfg['url'])
    sheet_name = cfg['sheet_name']
    
    print(f"Loading table '{table_name}' from {url} (Sheet: {sheet_name})...")
    try:
        df = pd.read_excel(url, sheet_name=sheet_name, engine='openpyxl')
        return df
    except Exception as e:
        print(f"Error loading table '{table_name}': {e}")
        return None

def load_sources_to_dataframes(yaml_path='_src_capillas.yml'):
    """
    Loads all tables defined in the YAML into pandas DataFrames as Excel files.
    """
    configs = get_source_config(yaml_path)
    dfs = {}
    
    for cfg in configs:
        name = cfg['name']
        df = load_table_to_dataframe(name, yaml_path)
        if df is not None:
            dfs[name] = df
            print(f"Head of {name}:")
            print(df.head())
            print("-" * 30)
            
    return dfs

if __name__ == "__main__":
    # Load and print heads of all tables
    loaded_dfs = load_sources_to_dataframes()

# get url