##Exercice 16
def solve16(n):
    #Ici n est le nombre dont on essaie de sommer les chiffres
    L=str(n)
    L=list(L)
    for i in range(len(L)):
        L[i]=int(L[i])
        
    assert solve16(25)==7
    return sum(L)


