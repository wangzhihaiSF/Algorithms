# leetcode 350, 求交集
class Solution(object):
    # 自己想的
    def intersect1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        new_list = []
        for i in nums1:
            if i in nums2:
                new_list.append(i)
                nums2.remove(i)  # 避免两个集合中相同元素次数不一致，添加重复
        return new_list

    # 新奇的脑回路
    def intersect2(self, nums1, nums2):
        inter = set(nums1) & set(nums2)
        l = []
        for i in inter:
            l += [i] * min(nums1.count(i), nums2.count(i))
        return l

    # 双指针
    def intersect3(self, nums1, nums2):
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
    # result1 = so.intersect1(n1, n2)
    # result2 = so.intersect2(n1, n2)
    result3 = so.intersect3(n1, n2)
    # print(result1)
    # print(result2)
    print(result3)
    # print(n1.count(2))
    #
