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


def romanToInt(input_string):
    total_value = 0
    for i in range(0, len(input_string)):
        if input_string[i] in my_dict.keys():

        # return total_value


print(romanToInt("MCMXCIV"))
