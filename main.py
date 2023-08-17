class Atm:
    def __init__(self):
        self.__pin = "1234"
        self.__balance = 0

        self.menu()
    def menu(self):
        user_input = input("""
        Hello, how would you like to proceed?
        1. Enter 1 to create pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to exit
        """)
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.deposit()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.balance()
        elif user_input == '5':
            print('Exit')
    def create_pin(self):
        self.__pin = input("Enter your pin:")
        print("pin set successfully!")

    def deposit(self):
         temp = input("Enter your pin:")
         if temp == self.__pin:
             amount = int(input("Enter the amount"))
             self.__balance = self.__balance + amount
             print("Deposit successful")
         else:
             print("Invalid pin!")
    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount:"))
            if amount < self.__balance:
                self.__balance = self.__balance - amount
                print("Withdraw successful")
            else:
                print("Insufficient balance!")
        else:
            print("Invalid pin!")
    def balance(self):
        temp = input("Enter your pin:")
        if temp == self.__pin:
            print("Your current balance is",self.balance)
        else:
            print("Invalid pin")

sbi = Atm()
