
class UserAccount:

    def __init__(self, own, num, bal):
        self.account_owner = own
        self.account_num = num
        self.account_balance = int(bal)

    def deposit(self, dep):
        self.account_balance += int(dep)

    def withdraw(self, wit):
        if self.account_balance > int(wit):
            self.account_balance -= int(wit)
        else:
            pass

    def __str__(self):  # string
        return f"Account Owner: {self.account_owner}\n" \
               f"Account Number: {self.account_num}\n" \
               f"Account Balance: {self.account_balance}"

    def __repr__(self):  # representation
        return f"UserAccount({self.account_owner}, {self.account_balance}, {self.account_balance})"
