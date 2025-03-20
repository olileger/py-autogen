import os
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from ag_Ext import *


class AssistantAgentHelper:

    def CreateFromFile(name, systemMessageFilePath, api_key, model = "4o"):
        with open(systemMessageFilePath, 'r') as file:
            systemMessage = file.read()
        
        return AssistantAgent(name=name,
                              system_message=systemMessage,
                              model_client=OpenAIChatCompletionClient(model=GetModelFullname(model), api_key=api_key))
    
    def CreateFromFileAndEnv(name, systemMessageFilePath, apikeyEnvVarName, model = "4o"):
        return AssistantAgentHelper.CreateFromFile(name, systemMessageFilePath, os.getenv(apikeyEnvVarName), model)