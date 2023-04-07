class Account:
    def __init__(self, id, parent_program, parent_program_subtype, data, tokens, version, callback_time_ms):
        """
        Class representing an account.

        Args:
            id (str): Unique identifier of the account.
            parent_program (str): Program that owns the account.
            parent_program_subtype (str): Subtype of the parent program.
            data (dict): Data of the account.
            tokens (int): Amount of tokens in the account.
            version (int): Version of the account on chain.
            callback_time_ms (int): The callback time in milliseconds associated with the account.
        """
        self.id = id
        self.parent_program = parent_program
        self.parent_program_subtype = parent_program_subtype
        self.data = data
        self.tokens = tokens
        self.version = version
        self.callback_time_ms = callback_time_ms

    def get_key(self):
        """
        Returns a key that represents the account. 
        Having this get_key function provides flexibility if we need to have a different identifier in the future

        Returns:
            str: An identifier of the account.
        """
        return f"{self.id}"

    def __str__(self):
        """
        Returns a string representation of the account.

        Returns:
            str: A string representing the account.
        """
        return f"{self.id}, {self.parent_program_subtype}, {self.version}"

