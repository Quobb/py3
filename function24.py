while True:
    n = int(input("enter a value : "))
    if n > 0:
        break

# for _ in range(n):
#     print("meow")


def chris(words):
    for i in range(words):
        n = i
        new = "*" * n
        blank = " " * (words - i)
        print(blank + new + "*"+ new)

print(chris(n))