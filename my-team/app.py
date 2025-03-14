import os
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient


def read_system_messages(path):
    with open(path, 'r') as file:
        return file.read()

def create_agent(name, systemMessage, api_key):
    return AssistantAgent(name=name,
                          system_messages=systemMessage,
                          chat_completion_client=OpenAIChatCompletionClient(api_key=api_key))


# Creating Agents
ac = create_agent("Le Correcteur", read_system_messages('./my-team/c.txt'), os.getenv('API_KEY'))
at = create_agent("Le Traducteur", read_system_messages('./my-team/t.txt'), os.getenv('API_KEY'))
ar = create_agent("Le Résumeur", read_system_messages('./my-team/r.txt'), os.getenv('API_KEY'))