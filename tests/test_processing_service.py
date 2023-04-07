import unittest
from unittest.mock import MagicMock
from models.account import Account
from services.processing_service import ProcessingService
from observers.highest_tokens_observer import HighestTokensObserver


class TestProcessingService(unittest.TestCase):
    """
    A class that contains unit tests for ProcessingService.
    """

    def setUp(self):
        """
        Sets up the objects needed for the tests.
        """
        self.service = ProcessingService()

    def test_attach_observer(self):
        """
        Tests if the attach_observer method adds an observer to the observers list.
        """
        observer = MagicMock()
        self.service.attach_observer(observer)
        self.assertEqual(len(self.service.observers), 1)

    def test_detach_observer(self):
        """
        Tests if the detach_observer method removes an observer from the observers list.
        """
        observer = MagicMock()
        self.service.attach_observer(observer)
        self.service.detach_observer(observer)
        self.assertEqual(len(self.service.observers), 0)

    def test_notify(self):
        """
        Tests if the notify method calls the update method of the observer with the given account.
        """
        observer = MagicMock()
        account = Account("id", "parent_program", "parent_program_subtype", "data", 100, 1, 1)
        self.service.attach_observer(observer)
        self.service.notify(account)
        observer.update.assert_called_with(account)

    def test_process_account_new_account(self):
        """
        Tests if the process_account method adds a new account to visited_accounts and notifies observers.
        """
        observer = HighestTokensObserver()
        account = Account("id", "parent_program", "parent_program_subtype", "data", 100, 1, 1)
        self.service.attach_observer(observer)
        self.service.process_account(account)
