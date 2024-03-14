def fact_rec(n):
    if n > 0:
        return n * fact_rec(n - 1)
    else:
        return 1


print(fact_rec(6))
