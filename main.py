def main():

    # the genome has a length of 25 EXCLUDING the 0 and 26 on the ends.
    melanoGenome = [0,23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9,26]
    mirandaGenome = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

    numberOfMutations = 0
    genome = melanoGenome

    while genome != mirandaGenome:
        numberOfMutations += 1
        genome = Mutate(genome)
        print(genome)
    print(numberOfMutations)


if __name__ == "__main__":
    main()
