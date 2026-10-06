def mod(T3, T1):
    s = T3.index(max(T3))
    print("mod = ", T1[s])


def med(T3, T1, n):
    s = 0
    for i in range(0, n - 1):
        if T3[i] >= 0.5:
            s = T3.index(T3[i])
            break
    print("med = ", T1[s])
