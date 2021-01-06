def subset_zero(L):
    '''The function take in a list L of numbers, return True only if there is a non-empty subset whose elements adds up to 0 '''
    neg = []
    pos = []

    # seperate negative and positive numbers
    for e in L:
        if e < 0:
            neg.append(e)
        elif e > 0:
            pos.append(e)
        else:
            return True  # if contains 0, automatically True

    if len(pos) == 0 or len(neg) == 0:
        return False  # if all neg or all pos, automatically False

    # create all possible sum from neg and pos
    neg = combine(neg)
    pos = combine(pos)

    for e in neg:
        if -e in pos:
            return True  # a sum in neg = a sum in pos

    return False


def combine(L):
    #total combination should be 2^n - 1, where n is len(L)

    if len(L) == 0:
        return []

    pre_combine = combine(L[1:])
    cur_combine = pre_combine[:]  # previous combine is a part of current combine
    cur_combine.append(L[0])  # itself is a part of current combine

    for e in pre_combine:
        cur_combine.append(e + L[0])  # itself + any element in previous combine is a part of current combine

    return cur_combine


L =  [4,10,20,-5,10,11,3.5,1.5]
print(subset_zero(L))
