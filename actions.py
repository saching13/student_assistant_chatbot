from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


from IPython.core.display import Image, display

import requests


class Action_retrieve_event(Action):
    def name(self):
        return 'action_retrieve_event'

    def run(self, dispatcher, tracker, domain):
        time = tracker.get_slot('time')
        # date = time.split('T')[0]
        # print("in custom chatbot")
        # r = requests.get('http://shibe.online/api/{}?count=1&urls=true&httpsUrls=true'.format(time))
        # response = r.content.decode()
        # response = response.replace('["',"")
        # response = response.replace('"]',"")

        # display(Image(response[0], height=550, width=520))
        dispatcher.utter_message("Here is something to cheer you up: ")

        return []