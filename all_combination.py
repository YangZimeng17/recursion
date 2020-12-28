#helper function
def combine(L,n):
    #list is not empty
    list = []
    length = len(L)
    for i in range(length + 1):
        if i == 0:
            list.append([n] + L)
        elif i == length:
            list.append(L + [n])
        else:
            list.append(L[:i] + [n] + L[i:])
    return list


def all_combination(L):
    if len(L) == 0:
        return []
    if len(L) == 1:
        return [L[:]]

    list = []
    for e in all_combination(L[:-1]):
        list = list + combine(e,L[-1])


    return list

list = ['a','b','c','d']
print(all_combination(list))