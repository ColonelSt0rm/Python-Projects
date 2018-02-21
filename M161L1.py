#Question 5
import math

def g(j):
    return 1/j

def sum(A, B):
    total = 0
    count = A
    while(count <= B):
        total = total + g(count)
        count = count + 1
    return total

def fillTable():
    k = 0
    lowestError = 1000
    while(k < 9 and lowestError > 0.01):
        print("k: "+str(k))

        N = 6*(2**k)
        print("N: "+str(N))

        A = 1+(2**k)
        print("A: "+str(A))

        B = 7*(2**k)
        print("B: "+str(B))

        print("g(j): "+str(g(A)))

        Sk = sum(A, B)
        print("Sk: "+str(Sk))

        Ek = abs(math.log(7) - Sk)
        print("Ek: "+str(Ek))

        if(Ek < lowestError):
            lowestError = Ek

        print("~~~~~~~~~~~~~~~~~~~~~")
        k = k + 1

    print("Iterations Complete!")
    print("Iteration stopped at k="+str(k-1))

fillTable()
