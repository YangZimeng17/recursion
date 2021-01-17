def is_fib(L):
    length = len(L)

    #base case
    if length == 0:
        return True
    if length == 1:
        if L[0] == 1:
            return True
        return False
    if length == 2:
        if L[0] == L[1] == 1:
            return True
        return False
    if length == 3:
        if L[0] == L[1] == 1 and L[2] == 2:
            return True
        return False

    #general
    if is_fib(L[:-1]) and L[-1] == (L[-2] + L[-3]):
        return True
    return False


test_lists = [[],[1],[0],[1,1],[1,2],[1,1,2],[1,2,3],[1,1,2,3,5,8,13],[5,8,13],[1,2,3,5,8]]

for e in test_lists:
    print(is_fib(e))
