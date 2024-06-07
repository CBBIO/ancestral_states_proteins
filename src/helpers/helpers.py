import pandas as pd
import yaml


def load_config(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config


def load_data(file_path):
    data = pd.read_csv(file_path)
    return data


def rename_columns(df):
    df['pdb_id_1'] = df['PDB1'].str[:4]
    df['chain_1'] = df['PDB1'].str[4:]
    df['pdb_id_2'] = df['PDB2'].str[:4]
    df['chain_2'] = df['PDB2'].str[4:]
    return df
