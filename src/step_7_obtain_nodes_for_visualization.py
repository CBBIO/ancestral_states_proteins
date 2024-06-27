import os
import pandas as pd

# Ruta del archivo de estados ancestrales
file_path = '/home/guest/PycharmProjects/ancestral_states_proteins/src/NR99.9MAFFT3j7vGOrg.fasta.state'

# Verifica la existencia del archivo
if not os.path.exists(file_path):
    print(f"El archivo {file_path} no existe. Verifica la ruta y el nombre del archivo.")
else:
    try:
        # Leer el archivo como un DataFrame de pandas
        df = pd.read_csv(file_path, sep='\t', comment='#')

        # Crear un diccionario para almacenar las secuencias ancestrales
        ancestral_sequences = {}
        print(df)
        # Agrupar por nodos y reconstruir secuencias
        for node, group in df.groupby('Node'):
            # Ordenar por 'Site' y unir los estados para formar la secuencia
            sequence = ''.join(group.sort_values('Site')['State'])
            ancestral_sequences[node] = sequence

        # Generar el archivo en formato FASTA
        output_file = '3j7vGLancestral_sequences.fasta'
        with open(output_file, 'w') as f:
            for node, seq in ancestral_sequences.items():
                f.write(f">{node}\n")
                f.write(f"{seq}\n")

        print(f"Archivo en formato FASTA generado: {output_file}")
    except Exception as e:
        print(f"Se produjo un error al leer el archivo: {e}")
