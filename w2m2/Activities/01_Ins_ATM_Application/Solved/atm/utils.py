"""Helper functions for loading accounts and validating PIN number."""

import csv
from pathlib import Path
import sys


def load_accounts():
    """Writes account information from CSV to list."""
    csvpath = Path('w2m2/Activities/01_Ins_ATM_Application/Solved/atm/accounts.csv')
    accounts = []
    print(csvpath.exists())
    print(csvpath.absolute())
    with open(csvpath, newline='') as csvfile:
        rows = csv.reader(csvfile)
        header = next(rows)
        for row in rows:
            pin = int(row[0])
            balance = float(row[1])
            account = {
                "pin": pin,
                "balance": balance
            }
            accounts.append(account)
        return accounts


def validate_pin(pin):
    """Verifies that PIN is 6 digits long."""

    # Verifies length of pin is 6 digits prints validations message and return True. Else returns False.
    if len(pin) == 6:
        print(f"The length of your PIN is valid")
        return True
    else:
        return False
