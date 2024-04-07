arr_input = [3, 2, 4]
target_value = 6


def twoSum(nums, target):
    listNum = {}
    n = len(nums)
    for i in range(n):
        complement = target - nums[i]
        if complement in listNum and listNum[complement] != i:
            return [i, listNum[complement]]
        listNum[nums[i]] = i


print(twoSum(arr_input, target_value))
