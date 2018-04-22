
def add(*args):
    return sum(args)


def add_long(*args):
    res = 0
    for i in args:
        res += i
    return res


if __name__ == '__main__':
    k = add(10, 20, 30, 40, 50)
    print(k)
    l = add_long(10, 20, 30, 40, 50)
    print(l)

