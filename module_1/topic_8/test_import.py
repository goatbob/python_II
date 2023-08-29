from OOP_assignment import *

account_1 = UserAccount("kyle", "00100", "1000")

account_2 = UserAccount("lauren", "00200", "500000")

if __name__ == "__main__":
    print(account_1)
    print(account_2)

    account_2.deposit("1000")
    print(account_2)

    account_1.withdraw("10000")
    print(account_1)
