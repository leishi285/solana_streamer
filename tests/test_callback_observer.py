import unittest
from unittest.mock import MagicMock, patch
from threading import Timer

from models.account import Account
from observers.callback_observer import CallbackObserver

class TestCallbackObserver(unittest.TestCase):

    def setUp(self):
        self.observer = CallbackObserver()
        self.account = Account(id=1, parent_program="Program A", parent_program_subtype="Subtype 1", data="data", tokens=10, version=1, callback_time_ms=5000)

    def tearDown(self):
        self.observer = None
        self.account = None

    @patch.object(Timer, 'start')
    def test_update(self, mock_timer_start):
        # Call update() method with a sample account object and assert that the Timer is started with the expected args
        self.observer.update(self.account)
        mock_timer_start.assert_called_with()
        self.assertEqual(len(self.observer.expirations), 1)

    def test_callback_expired(self):
        # Add a sample account to the expirations dict and call callback_expired() with the same account object
        self.observer.expirations[self.account.get_key()] = MagicMock(spec=Timer)
        self.observer.callback_expired(self.account)

        # Assert that the account's key is removed from expirations dict
        self.assertNotIn(self.account.get_key(), self.observer.expirations)
