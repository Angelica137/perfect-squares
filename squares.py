def squares_to_odd(a, b):
    total = (a*a) - (b*b)
    x = 2*b + 1
    y = 2*a - 1
    seq = ""
    while x < y:
        seq += str(x) + " + "
        x += 2
    seq += str(y)
    return f'{a}^2 - {b}^2 = {seq} = {total}'
