def bubble_sort(sequence):
    length = len(sequence)
    for i in range(length-1):
        for j in range(length-1-i):
            if sequence[j] > sequence[j+1]:
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
    return sequence


if __name__ == '__main__':
    numbers = [9, 21, 23, 90, 22, 67]
    bubble_sort(numbers)
    print(numbers)
