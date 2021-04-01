A = 10
B = 25
C = 15
L1 = [A,B,C,11,89,100,7]
def funcao (A,B,C,L1):
   
    print (L1)
    print (len(L1))
    L1.remove(A)
    L1.remove(B)
    L1.remove(C)
    print (L1)
    print (len(L1))
    
funcao (A,B,C,L1)
