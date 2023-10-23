class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print("Deposited Rs.{}. New balance: Rs.{}".format(
          amount, self.__account_balance))
    else:
      print("Invalid deposit amount. Please deposit a Positive amount.")

  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("Withdraw Rs.{}. New balance: Rs{}".format(amount,
                                                       self.__account_balance))
    else:
      print("invalid withdrawal amount or insufficient balance.")

  def display_balance(self):
    print("Account balance for {} (Account #{}): Rs{}".format(
        self.__account_holder_name, self.__account_number,
        self.__account_balance))


account = BankAccount(account_number="0123456789",
                      account_holder_name="Bharathi",
                      initial_balance=5000.00)
account.display_balance()
account.deposit(1000.00)
account.withdraw(3500.00)
account.display_balance()
