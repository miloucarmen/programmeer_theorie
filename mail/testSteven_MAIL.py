import helpersSteven_MAIL as helpersSteven

geno = [0,23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9,26]
mutationList = [(8, 12), (14, 24), (1, 4), (1, 3), (3, 15), (7, 8), (9, 12), (12, 25), (9, 22), (10, 21), (8, 11), (8, 20), (14, 18), (8, 17)]
genom = helpersSteven.GenomeSequence(geno)
for mutations in mutationList:
    genom.genome = genom.Reverse(mutations[0], mutations[1])
print(genom.genome)


# i = 1
# j = 2
# genome = [0, 1, 3, 2, 4]
# breakpointList = [1, 2, 3]
# newList = []
# for m in [i - 1, i, j, j + 1]:
#     print(m, breakpointList)
#     if abs(genome[m - 1] - genome[m]) == 1:
#         if m < len(genome) - 1:
#             if m in breakpointList and m not in newList:
#                 breakpointList.remove(m)

#         if m - 1 > 0:
#             if m - 1 in breakpointList and m - 1 not in newList:
#                 breakpointList.remove(m - 1)
#     else:
#         if m - 1 > 0:
#             breakpointList.append(m - 1)
#             newList.append(m - 1)
#         if m > 0:
#             breakpointList.append(m)
#             newList.append(m)

#     print(m, breakpointList)

#     if m + 1 < len(genome) :
#         if abs(genome[m] - genome[m + 1]) == 1:
#             if m in breakpointList and m not in newList:
#                 breakpointList.remove(m)
#             if m + 1 in breakpointList and m + 1 not in newList:
#                 breakpointList.remove(m + 1)
#         else:
#             if m + 1 < len(genome) - 1:
#                 breakpointList.append(m + 1)
#                 newList.append(m + 1)
#             breakpointList.append(m)
#             newList.append(m)

#     print(m, breakpointList)



# breakpointList = list(set(breakpointList))
# print("last", breakpointList)