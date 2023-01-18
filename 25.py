target = 282*9
def day25a():
    n = 1
    while n < target:
        if n % 2 == 0:
            n = n * 2 + 1
        else:
            n *= 2
    return n - target

print(day25a())