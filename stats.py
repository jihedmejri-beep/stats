from numpy
T1=[]
T2=[]
T3=[]
T4=[]
n=int(input("donner le nombre d'éléments:"))
def remplir(T1,T2):
    for i in range (n):
        T1[i]=float(input(""))
        T2[i]=float(input(""))
        N+=T1[i]
    return N

def frequence(T3,T2,N,n):
    for i in range (n):
            T3[i]=T2/N

def FFF(T3,T2,N,n):
    T4[0]=T3[0]
    for i in range (1,n-1):
         T4[i]=T4[i-1]+T3[i]
def mid(T4,T2,n):
    for i in range (n):
        if T4[i]>=0.5:
            print("the med is :",T2[i])
            break
def mod(T2,n):
    max=0
    for i in range (n):
        if T2[i]>max:
            max=T2[i]
    print("the mod:",max)



