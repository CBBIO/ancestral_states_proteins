from src.helpers.helpers import load_config, rename_columns, load_data
from src.pdb.pdb import get_amino_sequence


config = load_config('config/conf.yaml')
df = load_data(config['input_file'])
df = rename_columns(df)

df['seq_1'] = df.apply(lambda x: get_amino_sequence(x['pdb_id_1'], x['chain_1'], config), axis=1)
df['seq_2'] = df.apply(lambda x: get_amino_sequence(x['pdb_id_2'], x['chain_2'], config), axis=1)

df.drop('PDB1', axis=1, inplace=True)
df.drop('PDB2', axis=1, inplace=True)
df.dropna(inplace=True)

df.to_csv(config['output_file'], index=False)
