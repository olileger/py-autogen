import asyncio
import nest_asyncio
nest_asyncio.apply()

import os
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat, SelectorGroupChat
from autogen_agentchat.ui import Console


# Accès au modèle gpt4o.
gpt4o = OpenAIChatCompletionClient(
    model="gpt-4o-2024-08-06",
    api_key=os.getenv("API_KEY")
)

# On créé l'agent "Consultant".
consultant = AssistantAgent(
    "Consultant",
    model_client=gpt4o,
    system_message="Tu es un consultant spécialiste en opportunité business liées aux nouvelles technologies.",
)

# On créé l'agent "Revue".
reviewer = AssistantAgent(
    "Critique",
    model_client=gpt4o,
    system_message=
    """
    Tu es un agent qui génère un feedback clair et bienveillant afin que le consultant puisse modifier sa réponse.
    Tu dois faire des remarques sur la réponse du consultant et lui donner des conseils pour l'améliorer.
    Uniquement lorsque toutes tes remarques sont prises en compte, tu peux valider la réponse en répondant '## FIN ##'.
    """,
)

other_reviewer = AssistantAgent(
    "AutreCritique",
    model_client=gpt4o,
    system_message=
    """
    Tu produits un feedback par rapport à un texte donné.
    """
)

# On créé une condition d'arrêt pour le groupe de discussion.
approved = TextMentionTermination("## FIN ##")

# On créé le groupe de discussion avec les deux agents.
# team = RoundRobinGroupChat([consultant, reviewer], termination_condition=approved)
team = SelectorGroupChat([consultant, reviewer, other_reviewer],
                         gpt4o,
                         termination_condition=approved,
                         max_turns=10)

# On lance le groupe de discussion avec une tâche initiale.
async def main():
    await Console(team.run_stream(task=
    """
    Analyse l'état du marché de la GenAI et les opportunités business qui en découlent.
    Tu proposes ta réponse sous la forme d'une liste de 5 points de 3 phrases par point.
    """))

asyncio.run(main())