# Последовательность треугольных чисел образуется путем сложения натуральных чисел.
# К примеру, 7-ое треугольное число равно 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# Первые десять треугольных чисел:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Перечислим делители первых семи треугольных чисел:

#  1: 1
#  3: 1, 3
#  6: 1, 2, 3, 6
# 10: 1, 2, 5, 10
# 15: 1, 3, 5, 15
# 21: 1, 3, 7, 21
# 28: 1, 2, 4, 7, 14, 28
# Как мы видим, 28 - первое треугольное число, у которого более пяти делителей.

# Каково первое треугольное число, у которого более пятисот делителей?
import Utils


def task_12(divisors_count_barrier: int = 500):
    # Стартуем с 7-го по счету тругольного числа
    divisors_count = 6
    triangle_num_index = 7

    # Вычисляем все по очереди треугольные числа и кол-во их делителей,
    # пока число делителей не превысит divisors_count_barrier
    while divisors_count < divisors_count_barrier:
        triangle_num_index += 1
        triangle_num = Utils.get_triangle_num(triangle_num_index)
        divisors_count = Utils.count_num_divisors(triangle_num)

    print(triangle_num, ": первое треугольное число с числом делителей (",
          divisors_count, ") > 500")
    print("Треугольное число N:", triangle_num_index)


Utils.run_task(task_12)
