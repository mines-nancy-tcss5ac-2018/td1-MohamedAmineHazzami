##Exercice 55
def palindrome(n):
    #Vérifie si n est un palindrome
    L=list(str(n))
    return L[::-1]==L
def flip(n):
    return int(str(n)[::-1])
def solve55(n):
    #n le nombre qu'on calcule le nombre de nombres de lychrel qui lui sont inférieurs
    assert n<=10000,"Ne peut pas conclure, veuillez entrer un nombre <= 10000"
    Nombre=0
    for i in range(n+1):
        k=i
        compteur=0
        while compteur<50:
            if palindrome (k):
                break
            k+= flip(k)
            compteur+=1
            if compteur ==50:
                Nombre+=1
    return Nombre