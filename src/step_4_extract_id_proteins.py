import re

def clean_fasta_headers(input_fasta, output_fasta):
    with open(input_fasta, 'r') as infile, open(output_fasta, 'w') as outfile:
        for line in infile:
            if line.startswith('>'):
                # Utilizamos una expresión regular para limpiar el encabezado
                cleaned_header = re.match(r'^>([A-Za-z0-9_]+)', line)
                if cleaned_header:
                    outfile.write(cleaned_header.group(1) + '\n')  # Escribir solo el ID sin el carácter '>'
            else:
                continue

if __name__ == "__main__":
    input_fasta = '/home/guest/PycharmProjects/ancestral_states_proteins/src/NR99.9MAFFT3j7vG.fasta'  # Archivo FASTA de entrada
    output_fasta = '/home/guest/PycharmProjects/ancestral_states_proteins/src/Encabezados'  # Archivo FASTA de salida con encabezados limpios
    clean_fasta_headers(input_fasta, output_fasta)
    print(f"Cleaned FASTA saved to {output_fasta}")
