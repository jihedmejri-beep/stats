from numpy import *
n=int(input("donner le nombre d'éléments:"))
T0 = zeros((n, 2))
T1=array([0.0]*n)
T2=array([0.0]*n)
T3=array([0.0]*n)
T4=array([0.0]*n)

def remplir_num(T1,T2):
    for i in range (n):
        T1[i]=float(input("the x"+str(i)+":"))
        T2[i]=float(input("the n"+str(i)+":"))
    
    print(T1)
    print(T2)

def remplir_intervals(T0,T2):
    for i in range (n):
        T0[i][0]=float(input("the first half of x"+str(i)+":"))
        T0[i][1]=float(input("the second half of x"+str(i)+":"))
        T2[i]=float(input("the n"+str(i)+":"))
    
    print(T0)
    print(T2)
def get_xi(T0,T1):
    for i in range (n):
        T1[i]=(T0[i][0]+T0[i][1])/2
    print(T1)
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
    i=where(max(T3)==T3)[0][0]
    if not g :
        print("mode =", T1[i])
    else: 
        print("mode =", T0[i])
        
def median(T4,T1,n):
    for i in range (n):
        if T4[i]>=0.5:
            if not g :
                print("mediane =", T1[i])
                break
            else: 
                print("mediane =", T0[i])
                break
def mean (T1,T3,n):
    m=0
    for i in range (n):
        m+=T1[i]*T3[i]
    
    return m

def variance (T1,T3,n):
    m=mean(T1,T3,n)
    s=0
    for i in range (n):
        s+=T1[i]*T1[i]*T3[i]
        v=s-m*m
    return v

def deviation (T1,T3,n):
    v=variance(T1,T3,n)
    print ("deviation =", v**0.5)
global g
g=input("give 0 for numbers and 1 for intervals")
if g=="0":
    remplir_num(T1,T2)
else :
    remplir_intervals(T0,T2)
    get_xi(T0,T1)
N=nomber(T2,n)
frequence(T3,T2,N,n)
FFF(T3,T2,N,n)
mode(T3,T1)
median(T4,T1,n)
deviation(T1,T3,n)
print("mean =", mean(T1,T3,n))
print("variance =", variance(T1,T3,n))






