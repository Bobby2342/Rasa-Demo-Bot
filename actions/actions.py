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
from rasa_sdk.events import SlotSet




class ActionCheckBalance(Action):
    def name(self) -> Text:
        return "action_check_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        account_number = tracker.get_slot("account_number")
<<<<<<< HEAD
        #database dictionary 
=======
        phone = tracker.get_slot("phone")
        user_name = tracker.get_slot("name")
        
        
#database with Dict
>>>>>>> 18ee3a7 (update)
        database = {
            "1234567890": {"name": "Babim", "balance": 1000 , "phone": 9846863138},
            "0987654321": {"name": "Bishal", "balance": 2000, "phone": 9804109276},
        }
        
#validation 
        if account_number in database:
            user_info = database[account_number]
            user_name = user_info.get("name")
            balance = user_info.get("balance")
            phone = user_info.get("phone")
            dispatcher.utter_message(f"Dear {user_name}, \n your account number {account_number} \n has a balance of Rs. {balance}\n Your registered number is {phone}")
        else:
            dispatcher.utter_message("User not found in the database")

        return []
    


