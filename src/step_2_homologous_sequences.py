import os
import pyhmmer
from pyhmmer import easel, plan7

def load_aligned_fasta(filepath):
    # Usar MSA para cargar directamente el archivo FASTA alineado en formato 'afa'
    with easel.MSAFile(filepath, format="afa") as msa_file:
        text_msa = msa_file.read()
    # Digitalizar el MSA
    alphabet = easel.Alphabet.amino()
    digital_msa = text_msa.digitize(alphabet)

    return digital_msa


def build_hmm_from_msa(msa):
    builder = plan7.Builder(alphabet=easel.Alphabet.amino())
    background = plan7.Background(easel.Alphabet.amino())
    msa.name = b"protein_family_01"
    hmm, _, _ = builder.build_msa(msa, background)
    return hmm

def main():
    # Ruta al archivo FASTA alineado
    filepath = '/home/guest/PycharmProjects/ancestral_states_proteins/data/outputs/msa_results/aligned_1ceeB_2k42A.fasta'

    # Cargar el MSA digitalizado
    digital_msa = load_aligned_fasta(filepath)

    # Crear un modelo HMM a partir del MSA digitalizado
    hmm = build_hmm_from_msa(digital_msa)

    # Definir la ruta del archivo HMM de salida
    output_dir = '/home/guest/PycharmProjects/ancestral_states_proteins/data/outputs/profiles'
    hmm_path = os.path.join(output_dir, 'protein_family_01.hmm')

    with open(hmm_path, "wb") as output_file:
        hmm.write(output_file)

    # Imprimir alguna información básica sobre el modelo HMM creado
    print(f"HMM created with {hmm.M} states and written to {hmm_path}")

    alphabet = pyhmmer.easel.Alphabet.amino()
    background = pyhmmer.plan7.Background(alphabet)

    pipeline = pyhmmer.plan7.Pipeline(alphabet, background=background)

    # Crear una lista para almacenar las secuencias de los hits
    all_hits_sequences = []

    with pyhmmer.easel.SequenceFile(
            '/home/guest/PycharmProjects/ancestral_states_proteins/data/inputs/uniref50.fasta',
            digital=True, alphabet=alphabet) as seq_file:
        hits = pipeline.search_hmm(hmm, seq_file)

        # Recorrer los hits y obtener sus secuencias
        for hit in hits:
            # Obtener la secuencia del hit
            seq = seq_file.read_sequence(hit.offset, hit.length)

            # Almacenar la secuencia del hit
            all_hits_sequences.append(seq)

    # Definir la ruta del archivo FASTA de salida que contendrá todas las secuencias de los hits
    all_hits_fasta_path = '/home/guest/PycharmProjects/ancestral_states_proteins/data/outputs/homologous'

    # Escribir todas las secuencias de los hits en el archivo FASTA de salida
    with open(all_hits_fasta_path, 'w') as fasta_out:
        for i, seq in enumerate(all_hits_sequences, start=1):
            fasta_out.write(f'>Hit_{i}\n{seq}\n')

    print(f"Todas las secuencias de los hits han sido guardadas en {all_hits_fasta_path}")


if __name__ == "__main__":
    main()
