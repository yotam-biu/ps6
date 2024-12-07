def create_codon_dict(file_path):
    file = open(file_path)
    rows = file.readlines()
    file.close()

    codons2aa={}
    for row in rows:
        cell = row.strip().split('/t')
        codons2aa[cell[0]] = cell[2]
    return codons2aa


