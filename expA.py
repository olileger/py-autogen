from dotenv import load_dotenv
import os
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient


async def get_weather(city: str) -> str:
    return f"The weather in {city} is 73 degree and sunny."

async def main() -> None:
    w_agent = AssistantAgent(name="Weather_Agent",
                             model_client=OpenAIChatCompletionClient(model="gpt-4o-2024-08-06", api_key=os.getenv("API_KEY")),
                             tools=[get_weather])

    agent_team = RoundRobinGroupChat([w_agent], max_turns=1)

    while True:
        user_input = input("Enter a message (type 'exit' to leave): ")
        if user_input.strip().lower() == "exit":
            break
        stream = agent_team.run_stream(task=user_input)
        await Console(stream)


import asyncio
asyncio.run(main())