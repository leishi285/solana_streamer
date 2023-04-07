class HighestTokensObserver:
    def __init__(self):
        self.highest_tokens = {}

    def update(self, account):
        """
        Updates the highest tokens for a given parent_program_subtype.

        :param account: Account object
        """
        key = account.parent_program_subtype
        if key in self.highest_tokens:
            if account.tokens > self.highest_tokens[key].tokens:
                self.highest_tokens[key] = account
        else:
            self.highest_tokens[key] = account

    def print_highest_tokens(self):
        """
        Prints the highest tokens for each parent_program_subtype.
        """
        for key, account in self.highest_tokens.items():
            print(f"Highest tokens for {key}: {account.tokens} with version {account.version}")

    def notify_shutdown(self):
        # cleanup and shutdown
        print("HighestTokens observer shutting down")