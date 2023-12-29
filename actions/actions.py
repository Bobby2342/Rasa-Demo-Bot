# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCheckBalance(Action):
    def name(self) -> Text:
        return "action_check_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        account_number = tracker.get_slot("account_number")
        #database dictionary 
        database = {
            "1234567890": {"name": "Alice", "balance": 1000},
            "0987654321": {"name": "Bob", "balance": 2000}
            # Add more user information...
        }

        if account_number in database:
            user_info = database[account_number]
            user_name = user_info.get("name")
            balance = user_info.get("balance")
            dispatcher.utter_message(f"Dear {user_name}, your account number {account_number} has a balance of Rs. {balance}")
        else:
            dispatcher.utter_message("User not found in the database")

        return []
