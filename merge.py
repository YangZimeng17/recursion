def merge(L1, L2):
    #end point
    if len(L1) == 0:
        return L2[:]
    if len(L2) == 0:
        return L1[:]

    if L1[-1] > L2[-1]:
        return merge(L1[:-1], L2[:]) + [L1[-1]]
    return merge(L1[:], L2[:-1]) + [L2[-1]]

L1 = [4,8,10]
L2 = [2,4,6]

print(merge(L1, L2))

