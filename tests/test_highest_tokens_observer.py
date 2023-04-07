import unittest
from models.account import Account
from observers.highest_tokens_observer import HighestTokensObserver


class TestHighestTokensObserver(unittest.TestCase):
    def setUp(self):
        self.observer = HighestTokensObserver()

    def test_update_adds_account(self):
        account = Account('id1', 'parent_prog', 'subtype1', {'data': 1}, 10, 1, 1)
        self.observer.update(account)
        self.assertEqual(self.observer.highest_tokens['subtype1'], account)

    def test_update_updates_highest_tokens(self):
        account1 = Account('id1', 'parent_prog', 'subtype1', {'data': 1}, 5, 1, 1)
        account2 = Account('id2', 'parent_prog', 'subtype1', {'data': 2}, 10, 2, 1)
        self.observer.update(account1)
        self.observer.update(account2)
        self.assertEqual(self.observer.highest_tokens['subtype1'], account2)
