class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance        #making it private using underscore, so it cant be changed you get