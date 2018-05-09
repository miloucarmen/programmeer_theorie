import helpersSteven

genome = [0, 2, 1, 4, 6, 5, 3, 7]
print(genome)
genome = helpersSteven.GenomeSequence(genome)

print("i: ", 4)
print("j: ", 6)

genome = [0, 2, 1, 4, 3, 5, 6, 7, 2, 1]
genome.remove(10)
print(genome)
genome = helpersSteven.GenomeSequence(genome)


