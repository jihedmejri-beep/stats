n = int(input("donner le nombre d'éléments:"))
T1 = [0.0] * n
T2 = [0.0] * n
T3 = [0.0] * n
T4 = [0.0] * n


def remplir(T1, T2):
    for i in range(n):
        T1[i] = float(input("the x" + str(i) + ":"))
        T2[i] = float(input("the n" + str(i) + ":"))
    return T1, T2


def nomber(T2, n):
    N = 0.0
    for i in range(n):
        N += T2[i]
    if N == 0:
        raise ValueError("La somme des fréquences ne peut pas être nulle.")
    return N


def frequence(T3, T2, N, n):
    for i in range(n):
        T3[i] = T2[i] / N
    return T3


def FFF(T3, n):
    T4 = [0.0] * n
    T4[0] = T3[0]
    for i in range(1, n):
        T4[i] = T4[i - 1] + T3[i]
    return T4


def mean(T1, T3, n):
    m = 0.0
    for i in range(n):
        m += T1[i] * T3[i]
    return m


def variance(T1, T3, n):
    m = mean(T1, T3, n)
    s = 0.0
    for i in range(n):
        s += T1[i] * T1[i] * T3[i]
    return s - m * m


def deviation(T1, T3, n):
    v = variance(T1, T3, n)
    return v ** 0.5


remplir(T1, T2)
N = nomber(T2, n)
frequence(T3, T2, N, n)
T4 = FFF(T3, n)
m = mean(T1, T3, n)
v = variance(T1, T3, n)
d = deviation(T1, T3, n)

print(T1)
print(T2)
print(T3)
print(T4)
print("mean =", m)
print("variance =", v)
print("deviation =", d)





