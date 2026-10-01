class Client:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def show_info(self):
        print(f"{self.name} owes {self.amount}")


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show_info(self):
        print(f"{self.name} has {self.balance} Rupees")

    def deposit(self, amount):
        self.balance = self.balance + amount


client1 = Client("Ali", 5000)
client1.show_info()

amount1 = BankAccount("Zain", 23000)
amount2 = BankAccount("Hadia", 50000)
amount1.show_info()
amount2.show_info()

amount1.deposit(5000)
amount1.show_info()