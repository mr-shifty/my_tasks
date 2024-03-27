def merge_list(lst1, lst2):
    result_lst = []
    l_lst1 = len(lst1)
    l_lst2 = len(lst2)
    counter_a = counter_b = 0
    while counter_a < l_lst1 and counter_b < l_lst2:
        if lst1[counter_a] <= lst2[counter_b]:
            result_lst.append(lst1[counter_a])
            counter_a += 1
        else:
            result_lst.append(lst2[counter_b])
            counter_b += 1
    result_lst += lst1[counter_a:] + lst2[counter_b:]
    return result_lst


def split_and_merge(data):
    splited = len(data) // 2
    left = data[:splited]
    right = data[splited:]
    if len(left) > 1:
        left = split_and_merge(left)
    if len(right) > 1:
        right = split_and_merge(right)
    return merge_list(left, right)


print(split_and_merge([2, 1, 3, 2, 5, 10, 1, 4, 6, 3]))
