from numpy import array
T1=array([0.0]*n)
T2=array([0.0]*n)
T3=array([0.0]*n)
T4=array([0.0]*n)
n=int(input("donner le nombre d'éléments:"))
def remplir(T1,T2):
    for i in range (n):
        T1[i]=float(input("the x"+str(i)+":"))
        T2[i]=float(input("the n"+str(i)+":"))
    print(T1)
    print(T2)

def nomber(T2,n):
    N=0
    for i in range (n):
        N+=T2[i]
    return N

def frequence(T3,T2,N,n):
    for i in range (n):
            T3[i]=T2[i]/N
    print(T3)
    

def FFF(T3,T2,N,n):
    T4[0]=T3[0]
    for i in range (1,n):
         T4[i]=T4[i-1]+T3[i]
    print(T4)

def mode(T3,T1):
    print("mode =", T1[T3.index(max(T3))])

def mediane(T4,T1,n):
    for i in range (n):
        if T4[i]>=0.5:
            print("mediane =", T1[i])
            break

def MVD (T1,T3,n):
    m=0
    for i in range (n):
        m+=T1[i]*T3[i]
    print ("mean =", m)
    s=0
    for i in range (n):
        s+=T1[i]*T1[i]*T3[i]
    print ("variance =", s-m*m)
    print ("deviation =", (s-m*m)**0.5)


remplir(T1,T2)
N=nomber(T2,n)
frequence(T3,T2,N,n)
FFF(T3,T2,N,n)
mode(T3,T1)
mediane(T4,T1,n)
MVD(T1,T3,n)





