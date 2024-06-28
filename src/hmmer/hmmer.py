import pyhmmer


def build_hmm(fasta_path, background):
    with open(fasta_path, "rb") as f:
        seqs = pyhmmer.easel.SequenceFile(f)

        builder = pyhmmer.plan7.Builder(alphabet=pyhmmer.easel.Alphabet.amino())
        hmm = builder.build(seqs, background)
        return hmm



