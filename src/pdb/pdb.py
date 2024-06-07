from Bio.PDB import PDBList, PDBParser


def get_amino_sequence(pdb_id, chain, config):
    try:
        pdbl = PDBList(server=config['pdb_server'], pdb=config['pdb_dir'])
        parser = PDBParser()
        file_path = pdbl.retrieve_pdb_file(pdb_id, pdir=config['pdb_dir'], file_format='pdb')
        structure = parser.get_structure(pdb_id, file_path)
        for model in structure:
            for chain_obj in model:
                if chain_obj.id == chain:
                    return "".join([residue.resname for residue in chain_obj if
                                    residue.id[0] == ' '])
    except:
        return None
