def mult_by_2(value):
    return value * 2


times_two = mult_by_2

print("4 x 2 =", times_two(4))


def do_math(func, numb):
    return func(numb)


print("8 * 2 =", do_math(mult_by_2, 8))


def get_func_mult_by_numb(numb):
    def mult_by_value(value):
        return numb * value

    return mult_by_value


gen_func = get_func_mult_by_numb(5)
print("5 * 9 =", gen_func(9))

list_of_funcs = [mult_by_2, gen_func]
print("5 * 9 =", list_of_funcs[1](9))


def is_odd(numb):
    if numb % 2 == 0:
        return False
    else:
        return True


listNumb = [2, 6, 8, 9, 12, 14, 13, 17]
oddList = []
for num in listNumb:
    if is_odd(num):
        oddList.append(num)

print(oddList)
values_list = range(1, 21)
for i in values_list:
    print(i)