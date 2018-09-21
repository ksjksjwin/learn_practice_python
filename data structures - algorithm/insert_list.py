"""
insert number x in the List(ordered) with appropriate index (ordered)
"""
def solution(L, x):
    for i in range(0,len(L)):
        if x < L[i]:
            L.insert(i,x)
            return L
        else:
            continue
    L.insert(len(L),x)
    return L
