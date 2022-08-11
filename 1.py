def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end + 1))


a = int(input('Введите число:\n'))
b = int(input('Введите число:\n'))
print(sum_range(a, b))
