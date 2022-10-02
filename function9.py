# # program = input('Enter a program:')
# # b = compile(program,'something','exec')
# # exec(b)


# class Student:
#   marks = 0

#   def compute_marks(self, obtained_marks):
#     marks = obtained_marks
#     print('Obtained Marks:', marks)

# # convert compute_marks() to class method
# Student.print_marks = classmethod(Student.compute_marks)

# Student.print_marks(99)


# languages = ['Python', 'Java', 'JavaScript']

# enumerate_prime = enumerate(languages)
# print(list(enumerate_prime))


friends = ['champ','bill','billy','nabil','Quobbi','eli']

for item in enumerate(friends):
    print(item)


for list,item in enumerate(friends,10):
    print(list,item)

for item in enumerate(friends,3):
    print(item)