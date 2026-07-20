def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    hammingdis = 0

    for i, char in enumerate(strand_a):
        if strand_b[i] != char:
            hammingdis += 1
            
    return hammingdis
