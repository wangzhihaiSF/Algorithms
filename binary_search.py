from bubble_sort import bubble_sort


def binary_search(sequence, number, lower, upper):
    if number in sequence:
        if lower == upper:
            return lower
        else:
            middle = (lower+upper) // 2
            if number > sequence[middle]:
                return binary_search(sequence, number, middle+1, upper)
            else:
                return binary_search(sequence, number, lower, middle)


if __name__ == '__main__':
    numbers = [23, 2, 89, 12, 70, 11, 9, 55]
    numbers = bubble_sort(numbers)
    print(numbers)
    number = 89
    lower = 0
    upper = len(numbers)
    number_index = binary_search(numbers, number, lower, upper)
    print(number_index)
