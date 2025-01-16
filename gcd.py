import math

def euclidean_algorithm(x,y):
    
    factors_x = set(prime_factors(x))
    factors_y = set(prime_factors(y))
    res = 1

    for i in list(factors_x&factors_y):
      res = res*i
    return res
    
def prime_factors(n):
    
    factors = []
    # find the number of 2's
    while n%2==0:
        factors.append(2)
        n=n//2
    # Now n is odd
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            factors.append(i)
            n=n//i
    # last number which is left if greater than 2
    if n>2:
        factors.append(n)
    
    return factors
