def searchInsert(nums, target):
    indexer = 0
    temp = len(nums) // 2
    if target in nums:
        return nums.index(target)
    elif target >= nums[temp]:
        for i in range(temp, len(nums)):
            if nums[i] > target and nums[i] != nums[-1]:
                indexer = i
                break
            elif nums[i] > target and nums[i] == nums[-1]:
                indexer = i
                break
            elif nums[i] < target and nums[i] == nums[-1]:
                indexer = i + 1
                break
    else:
        for i in range(0, temp):
            if nums[i] > target:
                indexer = i
                break
            elif nums[i] < target:
                indexer = i + 1
                break

    return indexer


print(searchInsert([1,2,4,6,7], 3))
