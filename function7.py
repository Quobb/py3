from tkinter import TRUE


#this function checks if interger entered is prime number

def is_prime(n):
    for i in range(2,int(n/2)):
        if n % i == 0:
            return False
        else:
            return True


print(is_prime(6))