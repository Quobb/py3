def main():
    print_row(5)


def print_row(size):
    for i in range(size):
        for j in range(size):
            for x in range(size):
                print("#",end="")
            print()
        print()

main()