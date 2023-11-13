def filt(*args):
    value = []

    for item in args:
        if isinstance(item, str):
            value.append(item)

    print(args[len(args)-1])
    return value


print(filt(2, [4, 2], "qwdqwd", 5, 9.1, True, "koijij"))


my_list = [2, [4, 2], "qwdqwd", 5, 9.1, True,  "koijij"]

print(list(filter(lambda x: isinstance(x, str), my_list)))
