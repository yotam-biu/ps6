def create_codon_dict(file_path):
    file = open(file_path)
    rows = file.readlines()
    file.close()

    codons2aa={}
    for row in rows:
        cells = row.strip().split('\t')
        codons2aa[cells[0]] = cells[2]
    return codons2aa


