import math
import re
#nCk
def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0



#factorielle
def fact(x) :
    x=int(x)
    result = 1
    while (x>1) :
        result=result*x
        x=x-1
    return result


# Fonction partie entière E()
def E(x) :
    if (x == int(x)) :
        return x
    elif (x>=0) :
        return int(x)
    else :
        return -E(-x)-1

# Algorithme d'Euclide pour le pgcd
def pgcdIt(a,b) :
   while a%b != 0 :
      a, b = b, a%b
   return b

def pgcdRec(a,b):
    if a%b == 0:
        return b
    else:
        return pgcd(b, a%b)

#plus petit commun multiple
def ppmc(a,b) :
    return (a * b) / pgcd(a,b)

#verifier primier
def estP(n):
    if n == 0 or n== 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n))):
            if n%i == 0:
                return False
        return True

#decomposition en nombre premier

def decoP(n):
    l=[]
    if estP(n) or n == 1 or n == 0:
        l.append((n, 1))
    else:
        i=2
        while n//i != 0:
            j=0
            if n%i == 0:
                while n%i == 0:
                    j+=1
                    n= n//i
                l.append((i, j))
            else:
                i+=1

    return l

def comb(N,k): # from scipy.comb(), but MODIFIED!
    if (k > N) or (N < 0) or (k < 0):
        return 0
    top = N
    val = 1
    while (top > (N-k)):
        val *= top
        top -= 1
    n = 1
    while (n < k+1):
        val /= n
        n += 1
    return val
