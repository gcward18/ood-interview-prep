import math
import random


class Account:   
    def __init__(self, accountId: int, name: str, balance:int):
        self._accountId = accountId
        self.name = name
        self._balance = balance
        
    def getAccountId(self):
        return self._accountId

    def getBalance(self):
        return self._balance
    
    def deposit(self, amount:int):
        self._balance += amount
    
    def withdraw(self, amount:int):
        if amount > self._balance:
            raise ValueError("Not enough money in account to process withdraw request...")
        self._balance -= amount
        

class Transaction:
    def __init__(self, accountId: int, tellerId: int):
        self._accountId = accountId
        self._tellerId = tellerId
        
    def getAccountId(self):
        return self._accountId

    def getTellerId(self):
        return self._tellerId

    @staticmethod
    def getTransactionDescription(self):
        pass
        

class DepositTransaction(Transaction):
    def __init__(self, accountId: int, tellerId: int, amount: int):
        super().__init__(accountId=accountId, tellerId=tellerId)
        self._amount = amount
    
    def getTransactionDescription(self):
        return f"Deposit of {self._amount} for {self._accountId} processed by {self._tellerId}"


class OpenAccountTransaction(Transaction):
    def __init__(self, accountId: int, tellerId: int):
        super().__init__(accountId=accountId, tellerId=tellerId)
    
    def getTransactionDescription(self):
        return f"Account opened for {self._accountId} processed by {self._tellerId}"


class WithdrawTransaction(Transaction):
    def __init__(self, accountId: int, tellerId: int, amount: int):
        super().__init__(accountId=accountId, tellerId=tellerId)
        self._amount = amount
    
    def getTransactionDescription(self):
        return f"Withdraw of {self._amount} for {self._accountId} processed by {self._tellerId}"

class Teller:   
    def __init__(self, id):
        self._id = id
    
    def getId(self):
        return self._id

class BankSystem:
    def __init__(self, transactions: list[Transaction], accounts: list[Account]):
        self._transactions: list[Transaction] = transactions
        self._accounts: list[Account] = accounts
    
    def getAccount(self, accountId):
        return self._accounts[accountId]
    
    def getAccounts(self):
        return self._accounts
    
    def getTransactions(self):
        return self._transactions
    
    def getNewAccountId(self):
        return len(self._accounts)
    
    def getNewTransactionId(self):
        return len(self._transactions)
    
    def createAccount(self, name: str, tellerId: int):
        account = Account(self.getNewAccountId(), name, balance=0)
        self._accounts.append(account)
        
        transaction = OpenAccountTransaction(account.getAccountId(), tellerId=tellerId)
        self._transactions.append(transaction)
        return account.getAccountId()
    
    def deposit(self, accountId: int, tellerId: int, amount: int):
        account = self.getAccount(accountId=accountId)
        account.deposit(amount)
        
        transaction = DepositTransaction(accountId=accountId, tellerId=tellerId, amount=amount)
        self._transactions.append(transaction)
        return 
    
    def withdraw(self, accountId: int, tellerId: int, amount:int):
        account = self.getAccount(accountId=accountId)
        if amount > account.getBalance():
            raise Exception('insufficent funds')
        
        account.withdraw(amount)
        
        transaction = WithdrawTransaction(accountId=accountId, tellerId=tellerId, amount=amount)
        self._transactions.append(transaction)
        return

class BankBranch:
    def __init__(self, bank_system: BankSystem, cash_on_hand: int, address: str):
        self._tellers: list[Teller] = []
        self._address = address
        self._cash_on_hand = cash_on_hand
        self._system = bank_system
    
    def deposit(self, accountId: int, amount):
        if not self._tellers:
            raise Exception("No available Tellers")
        teller_id = self.getNextTeller()
        return self._system.deposit(accountId=accountId, tellerId=teller_id, amount=amount)
        
    def withdraw(self, accountId: int, amount):
        if amount > self._cash_on_hand:
            raise Exception("Branch does not have enough cash")
        if not self._tellers:
            raise Exception("Branch does not have any Tellers")
        self._cash_on_hand -= amount
        teller_id = self.getNextTeller()
        return self._system.withdraw(accountId=accountId, tellerId=teller_id, amount=amount)
        
    def openAccount(self, name: str):
        if not self._tellers:
            raise Exception("No available Tellers")
        teller_id = self.getNextTeller()
        return self._system.createAccount(name=name, tellerId=teller_id)

    def addTeller(self, teller: Teller):
        self._tellers.append(teller)
    
    def getNextTeller(self):
        idx = round(random.random() * len(self._tellers) - 1)
        return self._tellers[idx].getId()
    
    def collectCash(self, ratio):
        cash_to_collect = round(self._cash_on_hand * ratio)
        self._cash_on_hand -= cash_to_collect
        return cash_to_collect
    
    def provideCash(self, cash):
        self._cash_on_hand += cash

class Bank:
    def __init__(self, branches: list[BankBranch], system: BankSystem, total_cash: int):
        self._branches = branches
        self._bank_system = system
        self._total_cash = total_cash
    
    def add_branch(self, address: str, initial_funds: int):
        branch = BankBranch(self._bank_system, cash_on_hand=initial_funds, address=address)
        self._branches.append(branch)
        return branch

    def collect_cash(self, ratio: float):
        for branch in self._branches:
            cash_collected = branch.collectCash(ratio=ratio)
            self._total_cash += cash_collected
    
    def printTransactions(self):
        results = []
        for transaction in self._bank_system._transactions:
            results.append(transaction.getTransactionDescription())
        return results