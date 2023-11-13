import math


def lesenka(number):
    # Вычисление длины первой ступеньки
    n = 0.5 * (math.sqrt(8 * number + 1) - 1)

    if n % 1 == 0:
        n = int(n - 1)
    else:
        n = int(n)

    stup = [0] * (n + 1)
    stup[n] = n + 1
    i = n - 1
    summ = stup[n]

    # Построение первой пирамидки
    while i >= 0 and summ < number:
        stup[i] = stup[i + 1] - 1
        summ += stup[i]
        if summ > number:
            while summ > number:
                stup[i] -= 1
                summ -= 1
        # print(summ)
        i -= 1

    # Проверка первой пирамидки
    # for i in range(0, n + 1):
    #     print(f"stup [{i}]", stup[i])

    count = 1
    i = 0

    # Подсчет всех возможных видов пирамидки (разбирая кубики сверху-вниз)
    while i < n:
        while stup[i] > 0:
            stup[i] -= 1
            for j in range(i + 1, n):
                if (stup[j] + 1) < stup[j + 1]:
                    count += 1
            stup[n] += 1
            count += 1
        i += 1

    # Проверка последней пирамидки
    # for i in range(0, n + 1):
    #     print(f"stup [{i}]", stup[i])

    return count


print(lesenka(1000))
