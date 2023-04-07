from models.account import Account
from typing import List
import json


class LoadingService:
    def __init__(self):
        self.accounts = []

    def load_accounts(self, file_path: str) -> List[Account]:
        """
        Load accounts from a JSON file.

        Args:
            file_path (str): Path to the JSON file.

        Returns:
            List[Account]: A list of Account objects.
        """
        # Open the JSON file
        with open(file_path, 'r') as f:
            data = json.load(f)

        for entry in data:
            try:
                account = Account(entry['id'], entry['parentProgram'], entry['parentProgramSubType'], entry['data'], entry['tokens'], entry['version'], entry['callbackTimeMs'])
                self.accounts.append(account)
            except KeyError:
                # Some entries don't have version, we skip them.
                print(f"Skipping malformed account: {entry}")
                continue

        return self.accounts
