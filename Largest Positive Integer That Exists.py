def findMaxK(nums):
    largest = max(nums)
    smallest = min(nums)
    for i in nums:
        if i in nums and -i in nums and largest < i:
            largest = i
        else:
            largest = 0
    return largest


print(findMaxK([-1, 10, 6, 7, -7, 1]))
