# ATM Banking System Simulation

A console-based ATM banking system built in Python using Object-Oriented Programming principles.

## Features

- **Multiple account support** — accounts are managed via a dictionary keyed by account number
- **PIN authentication** with a 3-attempt lockout (account locks after 3 consecutive wrong PIN entries)
- **Deposit** and **withdrawal** with input validation
- **Balance inquiry**
- **Transaction history** tracking per account
- **Exception handling** for invalid input, insufficient balance, and invalid amounts

## Tech Stack

- Python 3
- Core OOP concepts: encapsulation (private attributes), class methods
- No external libraries — pure Python standard library

## Project Structure

```
├── account.py   # Account class: balance, PIN, transaction history, deposit/withdraw logic
├── atm.py       # ATM class: manages multiple accounts, menu-driven CLI
└── .gitignore
```

## How It Works

- `account.py` defines the `Account` class. Balance and PIN are stored as private attributes
  (prefixed with `_`) and can only be modified through the class's own methods
  (`deposit()`, `withdraw()`, `verify_pin()`), enforcing encapsulation.
- `atm.py` defines the `ATM` class, which holds a dictionary of `Account` objects and drives
  a menu-based command-line interface for login and transactions.

## How to Run

1. Make sure Python 3 is installed.
2. Clone this repository:
   ```
   git clone https://github.com/vigneshreddytripuram66/ATM-Banking-System.git
   ```
3. Navigate into the folder and run:
   ```
   python atm.py
   ```
4. Use one of the demo accounts to log in:
   - Account: `1001` | PIN: `1234`
   - Account: `1002` | PIN: `4321`

## Example Session

```
=== Welcome to the ATM Simulation ===
Enter account number: 1001
Enter PIN: 1234
PIN verified successfully.

--- ATM Menu ---
1. Check Balance
2. Deposit
3. Withdraw
4. Transaction History
5. Exit
```

## Possible Improvements

- Persist account data to a file or database (currently in-memory only, resets on exit)
- Support for multiple simultaneous users
- Logging of failed login attempts for security auditing