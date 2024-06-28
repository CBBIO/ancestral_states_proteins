from Bio.PDB import PDBList, PDBParser
from Bio.SeqUtils import seq1


def get_amino_sequence(pdb_id, chain_id, config):
    try:
        pdbl = PDBList(server=config['pdb_server'], pdb=config['pdb_dir'])
        parser = PDBParser()
        file_path = pdbl.retrieve_pdb_file(pdb_id, pdir=config['pdb_dir'], file_format='pdb')
        structure = parser.get_structure(pdb_id, file_path)
        for model in structure:
            for chain in model:
                if chain.id == chain_id:
                    sequence = ""
                    for residue in chain:
                        if residue.id[0] == ' ':  # Evitar heteroátomos
                            sequence += seq1(residue.resname)
                    return sequence
    except:
        return None