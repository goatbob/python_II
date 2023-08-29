
def how_many_integers():
    num = 0
    while num == 0:
        try:
            num = int(input("How many numbers would you like to input: "))
        except ValueError:
            print("Not a valid number.")
    return num


def enter_integers(n):
    entered_nums = []
    for x in range(n):
        try:
            num = int(input("Enter a number: "))
        except ValueError:
            print("Not a valid number")
        entered_nums.append(num)
    return entered_nums


def average_of_integers(l):
    s = 0
    for x in l:
        s = s + x
    avg = s / len(l)
    return avg


if __name__ == "__main__":
    a = how_many_integers()
    b = enter_integers(a)
    print(b)
    c = average_of_integers(b)
    print(c)
