from Bio import SeqIO

# Ruta de los archivos
fasta_file_path = '/home/guest/PycharmProjects/ancestral_states_proteins/src/residues_deletedNR99.93j7vG.fasta'
idmapping_file_path = '/home/guest/PycharmProjects/ancestral_states_proteins/src/idmapping_3j7vG(1).tsv'
output_fasta_file_path = '/home/guest/PycharmProjects/ancestral_states_proteins/src/residues_modified.fasta'

# Leer el archivo de mapeo y construir el diccionario de ID a organismo
id_to_organism = {}
with open(idmapping_file_path, 'r') as idmapping_file:
    for line in idmapping_file:
        parts = line.strip().split('\t')
        if len(parts) > 3:
            sequence_id, organism = parts[0], parts[3]
            id_to_organism[sequence_id] = organism

# Leer el archivo FASTA, modificar las descripciones y guardar el nuevo archivo
with open(fasta_file_path, 'r') as fasta_file, open(output_fasta_file_path, 'w') as output_fasta_file:
    fasta_sequences = SeqIO.parse(fasta_file, 'fasta')
    for seq_record in fasta_sequences:
        sequence_id = seq_record.id
        organism = id_to_organism.get(sequence_id, 'Unknown_organism')
        new_id = f"{seq_record.id} {organism}"
        seq_record.id = new_id
        seq_record.description = ''

        print(seq_record.id)
        SeqIO.write(seq_record, output_fasta_file, 'fasta')

print(f"Archivo FASTA modificado guardado como {output_fasta_file_path}")


