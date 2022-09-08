
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

class User:
    userList = {}
    def __init__(self, userName, userEmail, accountName):
        User.userList[(str(self))] = self
        self.userName = userName
        self.userEmail = userEmail
        self.accountName = accountName
        self.account = Bank_Account(0, .0125)
        self.accountDict = {self.accountName:self.account}
    def userDeposit(self, amount, acctName):
        self.accountDict[acctName].balance += amount
        print(f"user balance is now {self.account.balance}")
    def userWithdrawal(self, amount, acctName):
        self.accountDict[acctName].balance -= amount
        print(f"user balance is now {self.account.balance}")
    def userAcctInfo(self, acctName):
        print(self.accountDict[acctName].account_info())
    def addAccount(self, newName, newBalance, newRate):
        self.accountDict[newName]= Bank_Account(newBalance, newRate)
    @classmethod
    def transfer(cls,amount, user1, acctName1, user2, acctName2):
        cls.userList[str(user1)].userWithdrawal(amount,acctName1)
        cls.userList[str(user2)].userDeposit(amount,acctName2)
        
Samantha = User("Samantha", "sam@gmail.com","SamAcct")
Kyle = User("Kyle","Kyle@mybutt.com","KylesAcct")
Kyle.account.deposit(670)
Kyle.account.account_info()
Kyle.account.int_rate=1
Kyle.account.compound_int().compound_int().compound_int().account_info()
Kyle.userDeposit(444,"KylesAcct")
Kyle.userWithdrawal(222,"KylesAcct")
Kyle.userAcctInfo("KylesAcct")
Kyle.addAccount("KylesNewAccount",1300, .23)
Kyle.userAcctInfo("KylesNewAccount")
print(Kyle.accountDict)

User.transfer(50.00, Kyle,"KylesAcct",Samantha,"SamAcct") 
User.transfer(50.00, Samantha, "SamAcct", Kyle ,"KylesAcct")
