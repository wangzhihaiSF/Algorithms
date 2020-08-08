import time, datetime


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
                nums2.remove(i)
        return new_list

    # 新奇的脑回路
    def intersect2(self, nums1, nums2):
        same_item = set(nums1) & set(nums2)
        for i in same_item:
            same_item += [i] * min(nums1.count(i), nums2.count(i))
        return same_item

    # 双指针
    def intersect3(self, nums1: [int], nums2: [int]) -> [int]:
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
    start_time = datetime.datetime.now()
    print(start_time)
    so = Solution()
    n1, n2 = [1, 2, 2, 1], [2, 2]
    n = 0
    while n < 100:
        result =so.intersect1(n1, n2)
        n += 1
    # result = set(n1) & set(n2)
    end_time = datetime.datetime.now()
    print(end_time)
    change_time = end_time - start_time
    print(result)
    print(change_time)

