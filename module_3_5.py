def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        while str_number[-1] == '0':
            str_number = str_number[:-1]
            continue
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)
result3 = get_multiplied_digits(4008090)
print(result3)
result4 = get_multiplied_digits(1400000)
print(result4)
result5 = get_multiplied_digits(000000)
print(result5)