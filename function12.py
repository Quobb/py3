letter = 'champ billy quobbi'

def alphabet(letter):
    vowels = ['a','e','i','o','u']
    return True if letter in vowels else  False


champ = filter(alphabet,letter)

nab = list(champ)


print(nab)
hello 