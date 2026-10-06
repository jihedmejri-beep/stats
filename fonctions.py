def mean (T1,T3,n):
    m=0
    for i in range (n):
        m+=T1[i]*T3[i]
    print ("mean =", m)

def variance (T1,T3,n):
    m=mean(T1,T3,n)
    s=0
    for i in range (n):
        s+=T1[i]*T1[i]*T3[i]
    print ("variance =", s-m*m)

def deviation (T1,T3,n):
    v=variance(T1,T3,n)
    print ("deviation =", v**0.5)