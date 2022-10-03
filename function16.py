def linear_search(a, key):
	position = 0
	flag = False
	while position < len(a) and not flag:
		if a[position] == key:
			flag = True
		else:
			position = position + 1
	return flag


print(linear_search('champ','quabbi'))