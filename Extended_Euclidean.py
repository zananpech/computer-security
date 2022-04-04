

def recursive_extended_euclidean(a, b):

    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = recursive_extended_euclidean(b % a, a)

    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def iterative_extended_euclidean(a, b):
    i = 0
    x = [1, 0]
    y = [0, 1]
    while b != 0:
        q = a // b
        temp_x = x[0]
        temp_y = y[0]
        x[0] = x[1]
        y[0] = y[1]
        x[1] = x[1] * q + temp_x
        y[1] = y[1] * q + temp_y

        r = a % b
        a = b
        b = r

        i += 1
    return (a, x[0], -y[0]) if i % 2 == 0 else (a, -x[0], y[0])


def euclidean(a, b):

    while b != 0:
        r = a % b
        a = b
        b = r
    return a


if __name__ == "__main__":
    a = int(input("a: "))
    gcd, x, y = iterative_extended_euclidean(a=11, b=14)
    gcd, x, y = iterative_extended_euclidean(a=11, b=14)
    print(f"GCD={gcd}, x={x}, y={y}")
    print(f"GCD={gcd}, x={x}, y={y}")
