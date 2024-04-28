def removeDuplicates(List):
    new_list = List
    unique_n = 1
    i, j = 0, 1
    while i < len(new_list):
        if j >= len(new_list):
            break
        while j < len(new_list):
            if new_list[i] == new_list[j]:
                new_list.remove(new_list[j])
            else:
                unique_n += 1
                i += 1
                j += 1
                break
    return unique_n


print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
