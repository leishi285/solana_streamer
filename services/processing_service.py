class ProcessingService:
    """
    A service that processes accounts and notifies observers.
    """

    def __init__(self):
        """
        Initializes a ProcessingService object.
        """
        self.visited_accounts = {}
        self.observers = []

    def attach_observer(self, observer):
        """
        Attaches an observer to the list of observers.

        :param observer: The observer to be attached.
        """
        self.observers.append(observer)

    def detach_observer(self, observer):
        """
        Detaches an observer from the list of observers.

        :param observer: The observer to be detached.
        """
        self.observers.remove(observer)

    def notify(self, account):
        """
        Notifies all the observers with the given account.

        :param account: The account to be notified with.
        """
        for observer in self.observers:
            observer.update(account)

    def process_account(self, account):
        """
        Processes an account and notifies observers.

        :param account: The account to be processed.
        """
        key = account.get_key()

        if key in self.visited_accounts:
            if account.version > self.visited_accounts[key].version:
                print(f"Overwrote old verion {self.visited_accounts[key].version} with new version {account.version} under account {key}")
                self.visited_accounts[key] = account
            else:
                print(f"Ignoring update for account {key} since incoming version is older")
        else:
            self.visited_accounts[key] = account

        # Notify observers
        self.notify(self.visited_accounts[key])

        print(f"Indexed account {key} with tokens {account.tokens} and version {account.version}")

    
    def notify_shutdown(self):
        # Notify all observers of shutdown
        for observer in self.observers:
            observer.notify_shutdown()
