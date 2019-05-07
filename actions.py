from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import datetime
import mysql.connector
import datetime




class Action_retrieve_event(Action):
    def name(self):
        return 'action_retrieve_event'

    def run(self, dispatcher, tracker, domain):
        #time = tracker.get_latest_entity_values('time')
        #time = tracker.get_slot('time')
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database='chatbot'
        )
        #print(time)

        for d in tracker.latest_message['entities']:
            print(d['value'])
            if d['value'] != 'event':
                #parsed_date = datetime.datetime.strptime(str(d['value']).split('T')[0],"%Y-%m-%d")
                parsed_date = str(d['value']).split('T')[0]

                mycursor = mydb.cursor()
                #date = ('2019-04-17',)
                print(type(parsed_date))
                mycursor.execute("select event_name,start_time,end_time,venue from events where event_date = %s ",(parsed_date,))

                myresult = mycursor.fetchall()
                if len(myresult) > 0:
                    for d in myresult:
                        [name, start_time, end_time, location] = d

                        start_time = (datetime.datetime.min + start_time).time()
                        end_time = (datetime.datetime.min + end_time).time()
                        message  = "There is \"" + name + "\" at " + location
                        dispatcher.utter_message(message)
                        message = "Timings:" + str(start_time) + "-" + str(end_time)
                        dispatcher.utter_message(message)
                else:
                    message = "No events are happening on the requested date"
                    dispatcher.utter_message(message)

        #ent = tracker.latest_message['entities'][1][
        # 'value']
        #print(ent)

        # r = requests.get('http://shibe.online/api/{}?count=1&urls=true&httpsUrls=true'.format(time))
        # response = r.content.decode()
        # response = response.replace('["',"")
        # response = response.replace('"]',"")

        # display(Image(response[0], height=550, width=520))

        return []