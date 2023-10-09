import math
 
# A function to print all prime factors of
# a given number n
def primeFactors(n):
    # Print the number of two's that divide n
    list = []
    while n % 2 == 0:
        list.append(2)
        n = n // 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
         
        # while i divides n , print i ad divide n
        while n % i== 0:
            list.append(i)
            n = n // i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        list.append(n)
    return list
# Driver Program to test above function
 
 

def pwrs(g, n, B):
    for i in range(2, 100):
        eq = pow(g,i,n)
        ppf = primeFactors(eq)
        if(len(ppf) == 0):
            continue
        if(ppf[len(ppf)-1] <= B):
            print("{}{}{}{}{}".format(g, "^", i, ":\t", ppf))


pwrs(5, 43, 3)