T0=[] #use if you have intervals in form of lists

def turn_intervals_to_xi(T0,T1): #use if you have intervals in form of lists
    if not T1:
        for i in range(len(T0)) :
            interval=T0[i]
            T1= (interval[0] +interval [1])/2