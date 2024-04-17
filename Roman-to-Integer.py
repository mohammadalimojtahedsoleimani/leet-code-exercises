my_dict = {
    "I": 1,
    'V': 5,
    'X': 10,
    "L": 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
}
substrings_to_find = ["IV", "IX", "XL", "XC", 'CD', 'CM']


def romanToInt(input_string):
    skip_next = False
    total_value = 0

    for i in range(len(input_string)):
        if skip_next:
            skip_next = False  # Reset the flag
            continue
        if input_string[i:i + 2] in my_dict.keys():
            total_value += my_dict[input_string[i:i + 2]]
            skip_next = True
        else:
            total_value += my_dict[input_string[i]]

    return total_value


print(romanToInt("MCMXCIV"))
