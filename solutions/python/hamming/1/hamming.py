def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    lista = list(strand_a)
    listb = list(strand_b)
    hammingdis = 0

    for i in range(0, len(lista)):
        if lista[i] != (listb[i]):
            hammingdis += 1
            
    return hammingdis
