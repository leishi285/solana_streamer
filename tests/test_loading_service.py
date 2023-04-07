import os
import tempfile
import unittest
from unittest.mock import patch, mock_open
from models.account import Account
from services.loading_service import LoadingService


class TestLoadingService(unittest.TestCase):

    def setUp(self):
        self.service = LoadingService()

    def test_load_accounts(self):

        accounts = self.service.load_accounts("tests/data/tiny_data.json")
        assert len(accounts) == 2

        # Verify that each loaded account has the correct attributes
        for account in accounts:
            assert isinstance(account, Account)
            assert isinstance(account.id, str)
            assert isinstance(account.parent_program, str)
            assert isinstance(account.parent_program_subtype, str)
            assert isinstance(account.data, dict)
            assert isinstance(account.tokens, int)
            assert isinstance(account.version, int)
            assert isinstance(account.callback_time_ms, int)

        # Verify the attributes of a specific account
        assert accounts[0].id == "6BhkGCMVMyrjEEkrASJcLxfAvoW43g6BubxjpeUyZFoz"
        assert accounts[0].parent_program == "cndy3Z4yapfJBmL3ShUp5exZKqR3z33thTzeNMm2gRZ"
        assert accounts[0].parent_program_subtype == "mint"
        assert accounts[0].data == {"mintId": "6BhkGCMVMyrjEEkrASJcLxfAvoW43g6BubxjpeUyZFoz"}
        assert accounts[0].tokens == 243
        assert accounts[0].version == 5
        assert accounts[0].callback_time_ms == 500


    def test_load_accounts_skip_malformed_entries(self):
        accounts = self.service.load_accounts("tests/data/tiny_data_malformed.json")
        assert len(accounts) == 1

        assert all(isinstance(account, Account) for account in accounts)
        assert accounts[0].id == "6BhkGCMVMyrjEEkrASJcLxfAvoW43g6BubxjpeUyZFoz"