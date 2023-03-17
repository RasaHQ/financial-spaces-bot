from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionDoInvestment(Action):
    def name(self):
        return "action_do_investment"

    def run(self, dispatcher, tracker, domain):
        investment_type = tracker.get_slot("investment_type")
        if investment_type == "stocks":
            dispatcher.utter_message("You are interested in stocks")
        elif investment_type == "bonds":
            dispatcher.utter_message("You are interested in bonds")
        elif investment_type == "mutual funds":
            dispatcher.utter_message("You are interested in mutual funds")
        elif investment_type == "real estate":
            dispatcher.utter_message("You are interested in real estate")
        elif investment_type == "cryptocurrencies":
            dispatcher.utter_message("You are interested in cryptocurrencies")
        else:
            dispatcher.utter_message("You are interested in something else")
        return [SlotSet("display_options", True)]
