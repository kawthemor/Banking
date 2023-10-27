class Account:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self, profiles):
        self.accounts = {}
        self.create_accounts(profiles)

    def create_accounts(self, profiles):
        for name, initial_balance in profiles.items():
            self.accounts[name] = Account(initial_balance)

    def transfer(self, from_who, to_who, amt):
        if from_who in self.accounts and to_who in self.accounts:
            from_account = self.accounts[from_who]
            to_account = self.accounts[to_who]
            if from_account.get_balance() >= amt:
                from_account.withdraw(amt)
                to_account.deposit(amt)

    def get_names_in_debt(self):
        in_debt_names = [name for name, account in self.accounts.items() if account.get_balance() < 0]
        return in_debt_names

    def update_with_interest(self, interest_rate):
        for account in self.accounts.values():
            balance = account.get_balance()
            if balance > 0:
                interest = balance * interest_rate / 100
                account.deposit(interest)
            elif balance < 0:
                interest += balance * interest_rate / 100
                account.withdraw(interest)