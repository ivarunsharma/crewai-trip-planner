import os
from crewai import Agent, LLM
from textwrap import dedent

from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools


class TravelAgents:
    def __init__(self):
        self.azure_llm = LLM(
            model=f"azure/{os.getenv('AZURE_OPENAI_CHAT_DEPLOYMENT')}",
            base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            temperature=1,
        )

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(
                """I am a seasoned expert in travel planning and logistics.
                I specialize in creating memorable travel experiences."""
            ),
            goal="Plan a 7-day trip including daily itinerary, budget, packing tips and safety tips",
            tools=[
                SearchTools.search_internet,
                CalculatorTools.calculate
            ],
            verbose=True,
            llm=self.azure_llm
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(
                """Expert in analyzing travel trends and destinations."""
            ),
            goal="Select the best city based on weather, budget, and traveler interests",
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.azure_llm
        )

    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(
                """Local expert with deep knowledge of attractions, culture and hidden gems."""
            ),
            goal="Provide local insights and must-visit attractions",
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.azure_llm
        )