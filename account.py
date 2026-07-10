class Account:
    """
    Represents a single bank account.
    Holds balance, PIN, and transaction history.
    Balance and PIN are 'private' (prefixed with _) so they
    can only be changed through this class's own methods —
    this is encapsulation.
    """

    def __init__(self, account_number, pin, initial_balance=0):
        self.account_number = account_number
        self._pin = pin                      # private: no one edits this directly
        self._balance = initial_balance       # private: only changed via deposit/withdraw
        self.transaction_history = []
        self.failed_attempts = 0
        self.locked = False

    def verify_pin(self, entered_pin):
        """
        Checks entered PIN against the real one.
        Tracks failed attempts and locks the account after 3 wrong tries.
        """
        if self.locked:
            return False

        if entered_pin == self._pin:
            self.failed_attempts = 0   # reset on success
            return True
        else:
            self.failed_attempts += 1
            if self.failed_attempts >= 3:
                self.locked = True
            return False

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        self.transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient balance.")
        self._balance -= amount
        self.transaction_history.append(f"Withdrew: {amount}")

    def check_balance(self):
        return self._balance

    def show_history(self):
        if not self.transaction_history:
            return "No transactions yet."
        return "\n".join(self.transaction_history)