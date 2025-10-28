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