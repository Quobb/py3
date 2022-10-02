import math

def is_prime2(n):
    for i in range(2,int(math.sqrt(n/2)+1)):
        if n % i == 0:
            return False
        else:
            return True
        
        
print(is_prime2(17))