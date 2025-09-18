from bank_account import BankAccount


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