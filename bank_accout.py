class Bank_Account:
    bank_name = "nyc bank"
    all_accounts = []
    economy = {}
    def __init__(self, balance = 0.00, int_rate = 0.01):
        self.balance = balance
        self.int_rate = int_rate
        Bank_Account.all_accounts.append(self)
        Bank_Account.economy[str(self)] = self.balance
    def withdraw (self, amount):
        if amount > self.balance:
            pass
        else:
            self.balance = self.balance - amount
            Bank_Account.economy[str(self)] = self.balance
            print(f"your balance is now {self.balance} after witdrawing {amount}")
            return(self)
    def deposit (self, amount):
        self.balance = self.balance + amount
        Bank_Account.economy[str(self)]  = self.balance
        print(f"Your balance is now {self.balance} after depositing {amount}")
        return(self)
    def account_info(self):
        for x in vars(self):
            print(x,"=", str(vars(self)[x]))
            # print(x)
        return(self)
    def compound_int(self):
        self.balance = self.balance*(1+self.int_rate)
        Bank_Account.economy[str(self)] = self.balance
        print(f"your balance after compounding interest at {self.int_rate} is {self.balance}")
        return(self)
    @classmethod
    def print_inst(cls):
        for x in cls.all_accounts:
            print(x.account_info())
    @classmethod
    def total_econ(cls):
        sumof = 0
        for x in cls.economy:
            adder = cls.economy[x]
            sumof = adder + sumof
        print(sumof)



Kevin = Bank_Account(1000.25, .25)
# Kevin.deposit()
Kevin.account_info()
Kevin.compound_int()
Kevin.account_info()
Kevin.deposit(10000000.00)
Kevin.withdraw(10980)
Kevin.deposit(5.34)
Kevin.compound_int()
Kevin.account_info()
Kevin.deposit(12).deposit(66666666).deposit(987).withdraw(Kevin.balance*.99999).compound_int().account_info()

Carrie = Bank_Account(0.00, .5)
Carrie.account_info()
Carrie.deposit(1259.00).deposit(120).withdraw(345).withdraw(99).withdraw(99).compound_int().account_info()


Bank_Account.print_inst()
Bank_Account.total_econ()
print(Bank_Account.economy)


