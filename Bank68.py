class BankAccount:

    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance = balance

    def bygetter(self):
        return self.__balance

    def bysetter(self,amount):
        if amount>=0:
            self._balance = amount
        else:
           print("Invalid amount!")


obj = BankAccount("Janu",20000)

print(obj.bygetter())
print(obj.bygetter())
