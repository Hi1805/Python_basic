def tao_TD(Max):
    d = dict()
    for i in range(1, Max + 1):
        d[i] = i ** 2
    return d


def Print_Item(TD):
    for k, v in TD.items():
        print(k, v)


def Print_key(TD):
    for k in TD.keys():
        print(k)


def Print_value(TD):
    for v in TD.values():
        print(v)