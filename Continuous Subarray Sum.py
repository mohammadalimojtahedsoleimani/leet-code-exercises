def checkSubarraySum(nums, k):
    not_found = False
    summer = 0
    for i in range(len(nums)):
        summer += nums[i]
        for j in range(i+1, len(nums)):
            summer += nums[j]
            if nums[i] + nums[j]  % k == 0  or summer % k == 0:
                not_found = False
                return True
            else:
                not_found = True

        summer = 0
    if not_found:
        return False


print(checkSubarraySum([1,0,1,0,1], 4))
