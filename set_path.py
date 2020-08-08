class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int

        """
        res = 0
        ordered_set = {0}  # 保存已经能正确到达0的城市
        for (i, j) in connections:
            if j in ordered_set:  # j是已经能到0的城市，那么i->j后就可到0
                ordered_set.add(i)
            elif i in ordered_set:  # j目前不可到城市0，i可到，那就让j->i后到0，重修+1
                res += 1
                ordered_set.add(j)
        return res


if __name__ == '__main__':
    solu = Solution()
    n = 5
    connections = [[1, 0], [1, 2], [3, 2], [3, 4]]
    result = solu.minReorder(n, connections)
    print(result)
