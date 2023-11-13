def peresek(*args):
    value = args[0]
    cash = []
    for i in range(0, len(args) - 1):

        for j in range(0, len(value)):

            if value[j] in args[i + 1]:
                cash.append(value[j])

        value = cash  # Почему-то не могу перезаписать лист аргумента (args[i])
        cash = []

    return value


spisok_1 = [2, [4, 2], "qwdqwd", 5, False, 9.1, 8]
spisok_2 = ["qwdqwd", 5, 9.1, True, "koijij"]
spisok_3 = [5, 6, "qwdqwd", 7, 8, True]
spisok_4 = [9, 10, True, 5, 8, "qwdqwd"]

print(peresek(spisok_1, spisok_2, spisok_3, spisok_4))
