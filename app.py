from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig
from slack_token import slack_token


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/current')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)
#from rasa_core.utils import read_endpoint_config
#from rasa_core.agent import Agent

#endpoint_cfg = read_endpoint_config('endpoints.yml', 'action_endpoint')
#agent = Agent.load('models/dialogue', interpreter=nlu_interpreter,action_endpoint=endpoint_cfg)
## bot user authentication token
input_channel = SlackInput(slack_token)

agent.handle_channels([input_channel], 5004, serve_forever=True)