from threading import Timer

class CallbackObserver:
    def __init__(self):
        self.expirations = {}

    def update(self, account):
        key = account.get_key()

        if key in self.expirations:
            self.expirations[key].cancel()
            print(f"Cancelled the old callback for account {key}")
            del self.expirations[key]

        # Schedule new callback for the account, callback time is in second
        callback_time = account.callback_time_ms / 1000
        expiration = Timer(callback_time, self.callback_expired, args=[account])
        expiration.start()
        self.expirations[key] = expiration

    def callback_expired(self, account):
        key = account.get_key()

        if key in self.expirations:
            del self.expirations[key]
        print(f"Callback expired for account {key} with tokens {account.tokens} and version {account.version}")

    def notify_shutdown(self):
        # cleanup and shutdown
        print("Callback observer shutting down")
