def removeElement(nums, val):
    n = [x for x in nums]
    for i in range(len(nums)):
        if nums[i] == val:
            n.remove(nums[i])
    k = len(n)
    return k


print(removeElement([0,1,2,2,3,0,4,2], 2))



# correct version:
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         k = 0
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[k] = nums[i]
#                 k += 1
#
#         return k
