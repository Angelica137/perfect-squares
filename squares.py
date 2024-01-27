def squares_to_odd(a, b):
    total = (a*a) - (b*b)
    x = 2*b + 1
    y = 2*a - 1
    return f'{total}, {x}, {y}'
