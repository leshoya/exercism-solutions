def to_rna(dna_strand):
    translationtable = str.maketrans("GCTA", "CGAU")
    return dna_strand.translate(translationtable)
