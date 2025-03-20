import asyncio
import nest_asyncio
nest_asyncio.apply()

from ag_AgentChat_AgentsExt import AssistantAgentHelper
from ag_AgentChat_TeamsExt import TeamHelper
from autogen_agentchat.ui import Console


# Creating Agents
pr = AssistantAgentHelper.CreateFromFileAndEnv("Prompter", './better-prompt/pr.txt', 'API_KEY')
re = AssistantAgentHelper.CreateFromFileAndEnv("Reviewer", './better-prompt/re.txt', 'API_KEY')

t = TeamHelper.CreateDiscussionTeamFromEnv([pr, re], 'API_KEY')


async def main():
    await Console(t.run_stream(task=
    """
    Analyse l'état du marché de la GenAI et les opportunités business qui en découlent.
    Tu proposes ta réponse sous la forme d'une liste de 5 points de 3 phrases par point.
    """))

asyncio.run(main())