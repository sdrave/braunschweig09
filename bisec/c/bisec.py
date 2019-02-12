def bisec(f, a, b, tol=1e-4):
    while True:
        c = (a + b)/2
        y = f(c)
        if abs(y) < 1e-4:
            break
        if y > 0:
            b = c
        else:
            a = c

    return y

