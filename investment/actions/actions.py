from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionDoInvestment(Action):
    def name(self):
        return "action_do_investment"

    def run(self, dispatcher, tracker, domain):
        for investment_type in tracker.get_latest_entity_values("investment_type"):
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


class ActionShowStatus(Action):
    def name(self):
        return "action_show_status"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(response= "utter_financial_status", name = "Varun")
        return