#Use recursion to find the largest integer in the list L

def max_rec(L):
    #base case of recursion
    if len(L) == 0:
        return False
    if len(L) == 1:
        return L[0]

    #general case
    mid = len(L)//2
    max1 = max_rec(L[:mid])
    max2 = max_rec(L[mid:])

    if max1 > max2:
        return max1
    return max2

#test
print(max_rec([103,180,101,102,180]))
print(max_rec([103]))
print(max_rec([]))
print(max_rec([-2,-1,0,1,2]))