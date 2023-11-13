def check_int(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        if isinstance(result, int) == True:
            return result
        else:
            return "Вы ввели тип данных отличный от int"
    return wrapper


@check_int
def price_calculation(price, tax):
    return price * (1 + tax)


print(price_calculation(100, 0.05), "\n")

@check_int
def int_price_calculation(price, tax):
    return int(price * (1 + tax))


print(int_price_calculation(100, 0.05))
