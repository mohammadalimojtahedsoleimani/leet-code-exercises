def findMaxK(nums):
    temp = min(nums)
    largest = 0
    for i in nums:
        if i in nums and -i in nums and temp < i:
            largest = i
    return largest


print(findMaxK([-1,10,6,7,-7,1]))
