"""
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих
Начиная с 1 и 2, первые 10 элементов будут:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи,
которые не превышают четыре миллиона.
"""
import Utils


def task_2(limit: int = 4000000):
    fibo_row = []
    numbers = []
    summ = 0
    i = 1
    while True:

        if i < 3:
            number = i
            fibo_row.append(i)
        else:
            number = fibo_row[len(fibo_row) - 1] + fibo_row[len(fibo_row) - 2]
            fibo_row.append(number)
        if number > limit:
            print("Сумма: " + str(summ))
            break
        elif number % 2 == 0:
            numbers.append(number)
            summ += number
        i += 1
    print("Четные числа: ", numbers)
    print("Ряд Фиббоначи: ", fibo_row)


Utils.run_task(task_2)
