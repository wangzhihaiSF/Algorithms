# leetcode 350, 求交集
class Solution(object):
    # 自己想的
    @staticmethod
    def intersection1(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        new_list = []
        for i in nums1:
            if i in nums2:
                new_list.append(i)
                # 避免两个集合中相同元素次数不一致，添加重复, 这里只会删除第一个匹配项
                nums2.remove(i)
        return new_list

    # 新奇的脑回路
    @staticmethod
    def intersection2(nums1, nums2):
        inter = set(nums1) & set(nums2)  # 返回相同的元素，重复不计算
        l = []
        for i in inter:
            l += [i] * min(nums1.count(i), nums2.count(i))
        return l

    # 双指针
    @staticmethod
    def intersection3(nums1, nums2):
        nums1.sort()
        nums2.sort()
        r = []
        left, right = 0, 0
        while left < len(nums1) and right < len(nums2):
            if nums1[left] < nums2[right]:
                left += 1
            elif nums1[left] == nums2[right]:
                r.append(nums1[left])
                left += 1
                right += 1
            else:
                right += 1
        return r


if __name__ == '__main__':

    so = Solution()
    n1, n2 = [1, 2, 2, 1, 3], [2, 2, 1]
    result = so.intersection2(n1, n2)
    print(result)

