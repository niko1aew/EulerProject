""" Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
 Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
"""
import Utils


def task_4(search_range=range(999, 99, -1)):
    biggest_palindrom = 0
    num_a, num_b = 0, 0
    for i in search_range:
        for j in search_range:
            num = i * j
            if num > biggest_palindrom and Utils.palindrom_check(num):
                biggest_palindrom = num
                num_a, num_b = i, j
                break
    print(num_a, "*", num_b, "=", biggest_palindrom)
    print("Ответ: ", biggest_palindrom)


Utils.run_task(task_4)
