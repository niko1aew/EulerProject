"""
2^15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.

Какова сумма цифр числа 2^1000?
"""
import Utils


def Task_16(pow_num: int = 1000):
    str_num = str(2**pow_num)
    digit_sum = 0
    for char in str_num:
        digit_sum += int(char)
    print("Какова сумма цифр числа 2^1000:", digit_sum)


Utils.run_task(Task_16)
