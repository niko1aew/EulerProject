import datetime


def run_task(task):
    start_time = datetime.datetime.now()

    task()
    stop_time = datetime.datetime.now()
    print()
    print("Запущено: ", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("Остановлено: ", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("Время выполнения: ", str(stop_time - start_time))


def number_is_simple(n):
    if n == 1:
        return False
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n  # если квадратный корень из числа превышает само число, то число простое


def palindrom_check(number):
    number_str = str(number)
    number_reverse_str = number_str[::-1]
    return True if int(number) == int(number_reverse_str) else False


def get_num_divisors(num: int):
    quotient = num
    divisor = 2
    mnozhiteli = []
    while quotient > 1:
        if quotient % divisor == 0:
            mnozhiteli.append(divisor)
            quotient = quotient // divisor
        else:
            divisor += 1
    return mnozhiteli


def get_triangle_num(N: int):
    """
    Вычисляет N по счету треугольное число
    """
    assert N > 0
    triangle_num = 0
    for i in range(N, 0, -1):
        triangle_num += i
    return triangle_num


def count_num_divisors(num: int):
    """
    Вычисляет кол-во положительных делителей у заданного числа
    """
    # 1 Разложить число на множители
    mnozhiteli = get_num_divisors(num)

    # 2 Каноническое разложение
    iter_mnozhiteli = iter(mnozhiteli)
    Sn = []
    p = next(iter_mnozhiteli)
    s = 1
    for tmp in iter_mnozhiteli:
        if tmp == p:
            s += 1
        else:
            Sn.append(s)
            s = 1
        p = tmp
    Sn.append(s)

    result = 1
    for i in Sn:
        result *= (i + 1)
    return result
