"""
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

Найдите сумму всех простых чисел меньше двух миллионов.
"""
import Utils


def task_10():
    summ = 0

    for i in range(2000000):
        if Utils.number_is_simple(i):
            summ += i

    print(summ)


Utils.run_task(task_10)
