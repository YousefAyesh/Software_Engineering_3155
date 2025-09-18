from bank_account import BankAccount

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