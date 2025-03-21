import os
from autogen_ext.models.openai import OpenAIChatCompletionClient, AzureOpenAIChatCompletionClient

#
# ModelHelper
# This class is used to create model clients for OpenAI, Azure OpenAI and others.
#
class ModelHelper:

    def CreateModel(modelName, apikeyEnvVarName):
        modelName = ModelHelper._GetModelFullname(modelName)
        if apikeyEnvVarName.startswith("AOAI_"):
            return AzureOpenAIChatCompletionClient(model=modelName, api_key=os.getenv(apikeyEnvVarName))
        elif apikeyEnvVarName.startswith("OAI_"):
            return OpenAIChatCompletionClient(model=modelName, api_key=os.getenv(apikeyEnvVarName))

    def _GetModelFullname(model):
        if model == "4o":
                model = "gpt-4o-2024-08-06"
        elif model == "35t16":
            model = "gpt-3.5-turbo-16k"
        elif model == "35t32":
            model = "gpt-3.5-turbo-32k"
        return model