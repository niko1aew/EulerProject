"""
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.
Какое число является 10001-ым простым числом?
"""
def if_number_is_simple(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n # если квадратный корень из числа превышает само число, то число простое

input_num = 10001 # Порядковый номер простого числа, начиная от 2

nums_counter = 2
answer = 0
current_simple_num = 0
current_simple_num_counter = 0
while answer == 0:
    if if_number_is_simple(nums_counter):
        current_simple_num = nums_counter
        current_simple_num_counter+=1
        if current_simple_num_counter == input_num:
            print("10001-ое простое число: ", nums_counter)
            break
    nums_counter+=1
