from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import datetime


from IPython.core.display import Image, display

import requests


class Action_retrieve_event(Action):
    def name(self):
        return 'action_retrieve_event'

    def run(self, dispatcher, tracker, domain):
        time = tracker.get_latest_entity_values('time')
        #time = tracker.get_slot('time')

        print(time)

        for d in tracker.latest_message['entities']:
            print(d['value'])
            if d['value'] != 'event':
                parsed = datetime.datetime.strptime(str(d['value']).split('T')[0],"%Y-%m-%d")
                print(parsed)
        #ent = tracker.latest_message['entities'][1]['value']
        #print(ent)

        # r = requests.get('http://shibe.online/api/{}?count=1&urls=true&httpsUrls=true'.format(time))
        # response = r.content.decode()
        # response = response.replace('["',"")
        # response = response.replace('"]',"")

        # display(Image(response[0], height=550, width=520))
        dispatcher.utter_message("Here is something to cheer you up ")

        return []