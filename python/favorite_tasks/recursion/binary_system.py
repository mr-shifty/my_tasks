def get_binary_system(dig):
    if dig:
        print(dig % 2)
        get_binary_system(dig // 2)
    return None


get_binary_system(8)
get_binary_system(18)
