from numpy
T0=[] #use if you have intervals in form of lists
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

def turn_intervals_to_xi(T0,T1): #use if you have intervals
    if not T1:
        for i in range(len(T0)) :
            interval=T0[i]
            T1= (interval[0] +interval [1])/2