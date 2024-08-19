def singleNumber(nums):
    num_dict = {}
    for num in nums:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    for key, value in num_dict.items():
        if value == 1:
            return key


if __name__ == "__main__":
    print(singleNumber([2, 2, 1]))
