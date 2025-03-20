import os
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat, SelectorGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient
from ag_Ext import *


class TeamHelper:

    def CreateDiscussionTeamFromEnv(agents, apikeyEnvVarName, model = "4o", termination_condition = TextMentionTermination("## END ##"), max_turns = 10):
        return SelectorGroupChat(participants=agents,
                                 model_client=OpenAIChatCompletionClient(model=GetModelFullname(model), api_key=os.getenv(apikeyEnvVarName)),
                                 termination_condition=termination_condition,
                                 max_turns=max_turns)