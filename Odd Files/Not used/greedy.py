melanoGenome = [0,23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]

def greedy(genome):
    mirandaGenome = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    amount = 0

    # iterates till genome is ascending, and keep tracks of amount of mutations
    while genome != mirandaGenome:
        amount = amount + 1
        breakPoints = []

        # find all breaking points
        for i in range(len(genome) - 1):
            if abs(genome[i] - genome[i + 1]) != 1:
                breakpoints.append((genome[i], genome[i + 1]))

        # finds an 'optimum' switch to get rid of the highest amount of breaking points (2 max, 1 min, 0 = completed)
        for i in range(len(breakPoints)):


    return amount

if __name__ == "__main__":
    print(greedy(melanoGenome))
