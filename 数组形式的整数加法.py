"""
对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。

给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。

示例：

输入：A = [9,9,9,9,9,9,9,9,9,9], K = 1
输出：[1,0,0,0,0,0,0,0,0,0,0]
解释：9999999999 + 1 = 10000000000

"""
from functools import reduce
from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        return list(map(int, str(K + reduce(lambda a, b: a * 10 + b, A))))


if __name__ == '__main__':
    A = [2, 7, 4]
    K = 42
    result = Solution().addToArrayForm(A, K)
    print(result)
