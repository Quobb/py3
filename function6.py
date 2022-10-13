from pickle import TRUE


def prime(n):
    for i in range(2,n):
        if n % i == 0:
            return True
        else:
            return False
        
"""not working dont regard it"""
# list_numb = filter(prime,i)
# even_numb = list(list_numb)

# print(even_numb)

s = int(input("enter a number : "))
print(prime(s))
        