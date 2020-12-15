"""
冒泡排序，故名思议就像气泡漂上来一样，值比较小的在前，值比较大的在后。也可以反向排序
第一轮循环；拿第一个数和后面每个数比较
"""


def bubble_sort(sequence):
    length = len(sequence)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if sequence[j] > sequence[j + 1]:
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
    return sequence


if __name__ == '__main__':
    numbers = [9, 21, 23, 90, 22, 67]
    bubble_sort(numbers)
    print(numbers)
