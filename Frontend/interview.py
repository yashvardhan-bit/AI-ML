def nat(n):
    if n == 0:
        return 0

    return n+nat(n-1)

print(nat(6))