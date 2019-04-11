"""
Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?

Простое число - это натуральное число, имеющее ровно два делителя.
Составное число - число, имеющее больше двух делителей.
Исключение число "1". Оно имеет ровно один делитель - самого себя.
Делитель делит число без остатка.
Кратное число - это число, которое будем делить.

У каждого натурального числа, большего единицы, имеются по крайней мере два натуральных делителя: единица и само это число.
 При этом натуральные числа, имеющие ровно два делителя, называются простыми, а имеющие больше двух делителей — составными.
 Единица имеет ровно один делитель и не является ни простым, ни составным.

 Если нашли делитель без остатка, то частное этого деления тоже является делителем без остатка
"""
import Utils


def task_3(number: int = 13195):
    delitels = list()
    quotient = 0  # Частное от деления
    delitels.append(1)
    delitels.append(int(number))

    # Начинаем с "2", т.к. делить должен быть простым числом
    # Делитель не может быть больше, чем половина кратного числа
    # // означает, что от деления берем только целую часть числа
    for divisor in range(2, number // 2 + 1, 1):
        if number % divisor == 0:
            if divisor == quotient:
                break
            # Если нашли делитель без остатка, то частное этого деления тоже является делителем без остатка
            quotient = number / divisor
            delitels.append(int(divisor))
            delitels.append(int(quotient))  # Частное тоже делит без остатка

    delitels.sort()
    # Среди всех делителей ищем простые числа
    simple_delitels = list()
    for i in delitels:
        if i != 1 and Utils.number_is_simple(i):
            simple_delitels.append(i)

    print("Число: ", number)
    print("Все возможные делители без остатка: " + str(delitels))
    print("Все простые делители без остатка: " + str(simple_delitels))
    print("Самый большой делитель без остатка: " +
          str(simple_delitels[len(simple_delitels) - 1]))


Utils.run_task(task_3)
