"""
Тройка Пифагора - три натуральных числа a < b < c,
 для которых выполняется равенство a^2 + b^2 = c^2
Например, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc.
"""

import Utils


def task_9():
    solution_found = False

    for c in range(1000):
        if solution_found:
            break
        for b in range(1, c):
            if solution_found:
                break
            for a in range(1, c):
                if a < b < c and a + b + c == 1000 and a**2 + b**2 == c**2:
                    solution_found = True
                    print(a, b, c)
                    break


Utils.run_task(task_9)
