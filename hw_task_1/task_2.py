def max_str(a, b):
    if len(a) > len(b):
        return len(a)
    else:
        return len(b)


a = 'abc'
b = 'ab'
print(max_str(a, b))
