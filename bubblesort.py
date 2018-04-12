


def main():
    MELANOGASTER = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]

    # MIRANDA = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    print("{}".format(MELANOGASTER))
    bubblesort(MELANOGASTER)





def bubblesort(genoom):

    gesorteerdDeel = 1
    lengthGenome = len(genoom)


    while True:
        wissel = False
        for i in range(lengthGenome - gesorteerdDeel):

            if genoom[i] > genoom[i + 1]:
                genoom[i], genoom[i + 1] =  genoom[i + 1], genoom[i]
                wissel = True
        gesorteerdDeel += 1

        if not wissel:
            return(genoom)
        print("{}".format(genoom))


if __name__ == "__main__":
    main()


