
import pandas as pd
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio.Align.Applications import MafftCommandline
import os

def align_pair_of_sequences(seq1, seq2, id1, id2, aligned_fasta_path):
    # Crear SeqRecord para cada secuencia
    seq_record1 = SeqRecord(Seq(seq1), id=id1, description="")
    seq_record2 = SeqRecord(Seq(seq2), id=id2, description="")

    # Escribir las secuencias en un archivo FASTA temporal
    temp_fasta_path = 'temp_pair.fasta'
    SeqIO.write([seq_record1, seq_record2], temp_fasta_path, "fasta")

    # Ejecutar MAFFT para alinear las secuencias
    mafft_cline = MafftCommandline(input=temp_fasta_path)
    stdout, stderr = mafft_cline()

    # Escribir la alineación resultante en el archivo de salida
    with open(aligned_fasta_path, "w") as aligned_file:
        aligned_file.write(stdout)

def main():
    # Ruta al archivo CSV con los pares de secuencias
    csv_filepath = '/home/guest/PycharmProjects/ancestral_states_proteins/data/outputs/metamorphics.csv'

    # Leer el archivo CSV
    df = pd.read_csv(csv_filepath)

    # Crear un directorio para guardar las alineaciones si no existe
    output_dir = '/home/guest/PycharmProjects/ancestral_states_proteins/data/outputs/msa_results'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterar sobre cada fila (cada par de secuencias)
    for index, row in df.iterrows():
        id1 = row['PDB1']
        seq1 = row['seq_1']
        id2 = row['PDB2']
        seq2 = row['seq_2']

        # Definir la ruta del archivo FASTA alineado de salida para este par
        aligned_fasta_path = os.path.join(output_dir, f'aligned_{id1}_{id2}.fasta')

        # Alinear el par de secuencias y guardar el resultado
        align_pair_of_sequences(seq1, seq2, id1, id2, aligned_fasta_path)

        # Imprimir un mensaje indicando que la alineación para el par ha sido guardada
        print(f'Alineación para {id1} y {id2} guardada en {aligned_fasta_path}')

if __name__ == "__main__":
    main()
