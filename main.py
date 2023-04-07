from models.account import Account
from typing import List
import json
import os
import random
import time

from services.loading_service import LoadingService
from services.processing_service import ProcessingService
from observers.callback_observer import CallbackObserver
from observers.highest_tokens_observer import HighestTokensObserver

if __name__ == '__main__':
    # create loading service instance and load accounts from json file
    data_file_path = os.path.join(os.path.dirname(__file__), 'data/data.json')
    loading_service = LoadingService()
    accounts = loading_service.load_accounts(data_file_path)

    # create processing service instance and add observers
    processing_service = ProcessingService()

    # observers
    callback_observer = CallbackObserver()
    highest_token_observer = HighestTokensObserver()

    processing_service.attach_observer(callback_observer)
    processing_service.attach_observer(highest_token_observer)

    # process each account with random wait time and observers
    for account in accounts:
        # Random wait time between 0 and 1000ms
        wait_time = random.randint(0, 1000) / 1000
        time.sleep(wait_time)

        processing_service.process_account(account)

    # print the highest token-value accounts by subtype
    highest_token_observer.print_highest_tokens()

    # wait for all callbacks to finish
    while callback_observer.expirations:
        time.sleep(1)

    # Gracefully shut down
    processing_service.notify_shutdown()
    processing_service.detach_observer(callback_observer)
    processing_service.detach_observer(highest_token_observer)
    
    print("All accounts have been processed and there are no more expirations in the callback observer. Shutting down")
