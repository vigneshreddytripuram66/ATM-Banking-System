from account import Account


class ATM:
    """
    Manages multiple accounts using a dictionary:
        key   -> account_number
        value -> Account object

    This class is the 'front end' — it drives the menu and
    talks to Account objects, but never touches balance/pin directly.
    """

    def __init__(self):
        self.accounts = {}
        self._seed_demo_accounts()

    def _seed_demo_accounts(self):
        # A couple of demo accounts so the simulation has data to test with.
        self.accounts["1001"] = Account("1001", pin="1234", initial_balance=5000)
        self.accounts["1002"] = Account("1002", pin="4321", initial_balance=10000)

    def login(self, account_number, entered_pin):
        """
        Looks up the account and verifies the PIN.
        Returns the Account object if successful, else None.
        """
        account = self.accounts.get(account_number)

        if account is None:
            print("Account number not found.")
            return None

        if account.locked:
            print("Account is locked due to too many failed attempts.")
            return None

        if account.verify_pin(entered_pin):
            print("PIN verified successfully.\n")
            return account
        else:
            remaining = 3 - account.failed_attempts
            if account.locked:
                print("Incorrect PIN. Account is now locked.")
            else:
                print(f"Incorrect PIN. {remaining} attempt(s) remaining.")
            return None

    def run(self):
        print("=== Welcome to the ATM Simulation ===")
        account_number = input("Enter account number: ")

        account = None
        # allow up to 3 PIN attempts before giving up on this session
        for _ in range(3):
            entered_pin = input("Enter PIN: ")
            account = self.login(account_number, entered_pin)
            if account:
                break
            if self.accounts.get(account_number) and self.accounts[account_number].locked:
                break

        if account is None:
            print("Exiting. Too many failed attempts or invalid account.")
            return

        self._menu(account)

    def _menu(self, account):
        while True:
            print("\n--- ATM Menu ---")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transaction History")
            print("5. Exit")

            choice = input("Choose an option (1-5): ")

            try:
                if choice == "1":
                    print(f"Current Balance: {account.check_balance()}")

                elif choice == "2":
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                    print("Deposit successful.")

                elif choice == "3":
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                    print("Withdrawal successful.")

                elif choice == "4":
                    print("Transaction History:")
                    print(account.show_history())

                elif choice == "5":
                    print("Thank you for using the ATM. Goodbye!")
                    break

                else:
                    print("Invalid option. Please choose between 1-5.")

            except ValueError as e:
                # Catches both bad number input (e.g. typing letters)
                # AND our own raised errors like "Insufficient balance."
                print(f"Error: {e}")


if __name__ == "__main__":
    atm = ATM()
    atm.run()