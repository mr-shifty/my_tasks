def matryoshka(n: int):
    if n == 1:
        print("This is last matryoshka", n)
    else:
        print("top side of matryoshka", n)
        matryoshka(n - 1)
    print("bottom side of matryoshka", n)


if __name__ == "__main__":
    matryoshka(7)
