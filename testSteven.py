import helpersSteven

genome = [0, 2, 1, 25, 20, 19, 22, 23, 24, 11, 10, 7, 6, 5, 4, 3, 21, 17, 16, 15, 14, 13, 12, 18, 8, 9, 26]

print("The length of the genome equals: ", len(genome))
print("Element 0 equals: ", genome[0])
print("Element 26 equals: ", genome[26])

genome = helpersSteven.GenomeSequence(genome)

temp = genome.Reverse(0,1)
print(genome.Reverse(0,0))
print(temp)


