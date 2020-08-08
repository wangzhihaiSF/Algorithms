
def sortedSquares(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    B = []
    for i in A:
        B.append(i**2)
    B.sort()
    return B


if __name__ == '__main__':
    a = [-4,-1,0,3,10]
    print(sortedSquares(a))
