# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt
T = int(input())

def is_prime(n: int) -> bool:
    if (n % 2 == 0):
        False
    elif(n == 1):
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if (n % i == 0):
            return False
        
    return True
for i in range(T):
    n = int(input())
    if (is_prime(n)):
        print('Prime')
    else:
        print('Not prime')