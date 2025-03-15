# 将两个有序数组合并成一个，nums1长度足够容纳两个数组的元素
# 从后向前遍历，大的放在num1最后面

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2 = m - 1, n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p1 + p2 + 1] = nums1[p1]
                p1 -= 1
            else:
                nums1[p1 + p2 + 1] = nums2[p2]
                p2 -= 1
        while p2 >= 0:
            nums1[p2] = nums2[p2]
            p2 -= 1



