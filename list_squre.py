def sorted_squares(a):
    """
    :type a: List[int]
    :rtype: List[int]
    """
    b = []
    for i in a:
        b.append(i ** 2)
    b.sort()
    return b


if __name__ == '__main__':
    a = [-4, -1, 0, 3, 10]
    print(sorted_squares(a))
