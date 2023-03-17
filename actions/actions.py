from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionDemoGreet(Action):
    def name(self):
        return "action_demo_greet"

    def run(self, dispatcher, tracker, domain):
        print("Hello from the Financial Spaces Bot!")
        dispatcher.utter_message("Hello from the Financial Spaces Bot!")
        return []
