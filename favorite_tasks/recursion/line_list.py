def get_line_list(d, a=None):
    if a is None:
        a = []
    for data in d:
        if isinstance(data, list):
            get_line_list(data, a)
        else:
            a.append(data)
    return a


d = [
    1,
    2,
    [True, False],
    ["Москва", "Уфа", [100, 101], ["True", [-2, -1]]],
    7.89,
]

print(get_line_list(d))
