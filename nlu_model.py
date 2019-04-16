from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig



nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/current')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter=nlu_interpreter, action_endpoint=action_endpoint)



