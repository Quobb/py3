
"""checking for the even numbers"""

numbers = [1,2,3,4,6,7,8,9,10,11,24,26]

def check_even(numbers):
    if numbers % 2 == 0:
        return True
    return False


list_numb = filter(check_even,numbers)
even_numb = list(list_numb)

print( __doc__ ,even_numb)