def last_two(word):
    if len(word) < 2:
        return 'error'
    else:
        return word[-2:]


print(last_two('champ'))