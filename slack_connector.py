import slackclient,time
import chatbot_config

SOCKET_DELAY = 1

filepath = 'chatbot_config.py'
Slack_token = chatbot_config.Slack_token
slack_name = chatbot_config.slack_name
chatbot_id = chatbot_config.chatbot_id


chatbot_client = slackclient.SlackClient(Slack_token)

print(slack_name)
print(Slack_token)
is_ok = chatbot_client.api_call("users.list").get('ok')
print(is_ok)

if(is_ok):
    for user in chatbot_client.api_call("users.list").get('members'):
        if user.get('name') == slack_name:
            print(user.get('id'))


def is_for_me(event):
    """Know if the message is dedicated to me"""
    # check if not my own event
    type = event.get('type')
    if type and type == 'message' and not(event.get('user')==chatbot_id):
        # in case it is a private message return true
        if event.get('channel').startswith('D'): # means private Channel
            return True
        # in case it is not a private message check mention
        text = event.get('text')
        channel = event.get('channel')
        if slack_name in text.strip().split():
            return True


def handle_message(message, user, channel):

    post_message(message=say_hi(user_mention), channel=channel)


def post_message(message, channel):
    chatbot_client.api_call('chat.postMessage', channel=channel,text=message, as_user=True)


def run():
    if chatbot_client.rtm_connect():
        print('[.] Chatbot is ON...')
        while True:
            event_list = chatbot_client.rtm_read()
            if len(event_list) > 0:
                for event in event_list:
                    print(event)
                    if is_for_me(event):
                        handle_message(message=event.get('text'), user=event.get('user'),
                                       channel=event.get('channel'))
            time.sleep(SOCKET_DELAY)
    else:
        print('[!] Connection to Slack failed.')

if __name__ == '__main__':
    run()