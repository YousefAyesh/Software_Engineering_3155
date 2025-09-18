class BankAccount:
    bank = "First National Bank"

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = self._generate_account_number()
        self.__routing_number = "123456789"

    def _generate_account_number(self):
        import random
        return f"{random.randint(1000000000, 9999999999)}"

    def get_account_number(self):
        return self._account_number

    def get_routing_number(self):
        return self.__routing_number

    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"${amount:.2f} deposited successfully. New balance: ${self.current_balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        remaining_balance = self.current_balance - amount
        if remaining_balance < self.minimum_balance:
            print(f"Transaction denied. Withdrawal would leave balance (${remaining_balance:.2f}) "
                  f"below minimum required balance (${self.minimum_balance:.2f}).")
        else:
            self.current_balance -= amount
            print(f"${amount:.2f} withdrawn successfully. New balance: ${self.current_balance:.2f}")

    def print_customer_information(self):
        print("=" * 40)
        print(f"Bank: {self.bank}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self._account_number}")
        print(f"Routing Number: {self.__routing_number}")
        print(f"Current Balance: ${self.current_balance:.2f}")
        print(f"Minimum Balance: ${self.minimum_balance:.2f}")
        print("=" * 40)


class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        monthly_interest = self.current_balance * (self.interest_rate / 12)
        self.current_balance += monthly_interest
        print(f"Interest applied: ${monthly_interest:.2f}. New balance: ${self.current_balance:.2f}")

    def print_customer_information(self):
        print("=" * 50)
        print(f"SAVINGS ACCOUNT")
        print(f"Bank: {self.bank}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self._account_number}")
        print(f"Routing Number: {self.get_routing_number()}")
        print(f"Current Balance: ${self.current_balance:.2f}")
        print(f"Minimum Balance: ${self.minimum_balance:.2f}")
        print(f"Interest Rate: {self.interest_rate * 100:.2f}% annually")
        print("=" * 50)


class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, daily_transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.daily_transfer_limit = daily_transfer_limit
        self.daily_transfers_made = 0

    def transfer(self, amount, recipient_account):
        if amount <= 0:
            print("Transfer amount must be positive.")
            return

        if self.daily_transfers_made + amount > self.daily_transfer_limit:
            print(f"Transfer denied. Would exceed daily transfer limit of ${self.daily_transfer_limit:.2f}.")
            print(f"Today's transfers so far: ${self.daily_transfers_made:.2f}")
            return

        remaining_balance = self.current_balance - amount
        if remaining_balance < self.minimum_balance:
            print(f"Transfer denied. Would leave balance (${remaining_balance:.2f}) "
                  f"below minimum required balance (${self.minimum_balance:.2f}).")
            return

        self.current_balance -= amount
        self.daily_transfers_made += amount
        recipient_account.current_balance += amount

        print(f"${amount:.2f} transferred successfully to {recipient_account.customer_name}")
        print(f"Your new balance: ${self.current_balance:.2f}")
        print(f"Daily transfers used: ${self.daily_transfers_made:.2f} / ${self.daily_transfer_limit:.2f}")

    def reset_daily_transfers(self):
        self.daily_transfers_made = 0
        print("Daily transfer limit reset.")

    def print_customer_information(self):
        print("=" * 50)
        print(f"CHECKING ACCOUNT")
        print(f"Bank: {self.bank}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self._account_number}")
        print(f"Routing Number: {self.get_routing_number()}")
        print(f"Current Balance: ${self.current_balance:.2f}")
        print(f"Minimum Balance: ${self.minimum_balance:.2f}")
        print(f"Daily Transfer Limit: ${self.daily_transfer_limit:.2f}")
        print(f"Daily Transfers Made: ${self.daily_transfers_made:.2f}")
        print("=" * 50)


if __name__ == "__main__":
    print("Creating and testing BankAccount instances:\n")

    account1 = BankAccount("Yousef Ayesh", 1000.00, 100.00)
    account1.print_customer_information()

    print("\nTesting deposit:")
    account1.deposit(250.00)

    print("\nTesting valid withdrawal:")
    account1.withdraw(200.00)

    print("\nTesting withdrawal that exceeds limits:")
    account1.withdraw(1000.00)

    print("\n" + "=" * 50 + "\n")

    account2 = BankAccount("Bob Smith", 500.00, 50.00)
    account2.print_customer_information()

    print("\nTesting deposit:")
    account2.deposit(150.00)

    print("\nTesting withdrawal:")
    account2.withdraw(300.00)

    print("\nTesting withdrawal that would go below minimum:")
    account2.withdraw(400.00)

    print("\nFinal account information:")
    account1.print_customer_information()
    account2.print_customer_information()

    print("\n" + "=" * 70)
    print("TESTING NEW SUBCLASSES AND INHERITANCE FEATURES")
    print("=" * 70)

    print("\nCreating Savings Accounts:")
    savings1 = SavingsAccount("Alice Johnson", 5000.00, 500.00, 0.025)
    savings2 = SavingsAccount("Charlie Brown", 2500.00, 250.00, 0.03)

    print("\nCreating Checking Accounts:")
    checking1 = CheckingAccount("Emma Wilson", 3000.00, 100.00, 1000.00)
    checking2 = CheckingAccount("Diana Prince", 1500.00, 50.00, 500.00)

    print("\n" + "=" * 60)
    print("INITIAL ACCOUNT INFORMATION")
    print("=" * 60)

    savings1.print_customer_information()
    savings2.print_customer_information()
    checking1.print_customer_information()
    checking2.print_customer_information()

    print("\n" + "=" * 60)
    print("SCENARIO: User opens checking account and withdraws money")
    print("=" * 60)

    print("\n1. New customer opens checking account:")
    new_checking = CheckingAccount("Michael Scott", 2000.00, 200.00, 750.00)
    new_checking.print_customer_information()

    print("\n2. Customer makes a deposit:")
    new_checking.deposit(500.00)

    print("\n3. Customer withdraws money for expenses:")
    new_checking.withdraw(300.00)

    print("\n4. Customer attempts large withdrawal:")
    new_checking.withdraw(2000.00)

    print("\n5. Customer transfers money to Diana:")
    new_checking.transfer(400.00, checking2)

    print("\n6. Customer attempts another large transfer:")
    new_checking.transfer(500.00, checking2)

    print("\n" + "=" * 60)
    print("TESTING SAVINGS ACCOUNT FEATURES")
    print("=" * 60)

    print("\n1. Alice applies monthly interest:")
    savings1.apply_interest()

    print("\n2. Charlie makes a deposit then applies interest:")
    savings2.deposit(1000.00)
    savings2.apply_interest()

    print("\n" + "=" * 60)
    print("TESTING PROTECTED AND PRIVATE MEMBERS")
    print("=" * 60)

    print(f"\nAccessing account numbers through public methods:")
    print(f"Alice's account number: {savings1.get_account_number()}")
    print(f"Emma's routing number: {checking1.get_routing_number()}")

    print(f"\nDirect access to protected member: {savings1._account_number}")

    try:
        print(f"Trying to access private member directly: {savings1.__routing_number}")
    except AttributeError as e:
        print(f"Cannot access private member directly: {e}")
        print(f"But can access through public method: {savings1.get_routing_number()}")

    print("\n" + "=" * 60)
    print("FINAL ACCOUNT STATES - ALL ACCOUNTS")
    print("=" * 60)

    print("\nOriginal BankAccount instances:")
    account1.print_customer_information()
    account2.print_customer_information()

    print("\nSavings Account instances:")
    savings1.print_customer_information()
    savings2.print_customer_information()

    print("\nChecking Account instances:")
    checking1.print_customer_information()
    checking2.print_customer_information()
    new_checking.print_customer_information()