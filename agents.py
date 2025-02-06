from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
import os
from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools

from dotenv import load_dotenv
load_dotenv()
"""
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee 
    you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal. 
- Define which experts the captain needs to communicate with and delegate tasks to.
    Build a top down structure of the crew.

Goal:
- Create a vector structure of the code of the  repo fetch in github.

Captain/Manager/Boss:
- Project Manager

Employees/Experts to hire:
- Code Analyst

Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume
"""


class BackDevAgents:
    def __init__(self):
        self.GroqDeepSeek = ChatOpenAI(
            openai_api_base="https://api.groq.com/openai/v1",
            model_name="deepseek-r1-distill-llama-70b",
            openai_api_key=os.getenv("GROQ_API_KEY"),
            temperature=0.1
        )

    def code_analyst_agent(self):
        return Agent(
            role="Analyzes the code structure and identifies dependencies between its components.",
            backstory=dedent(
                f"""You are an expert in code analysis and code structure for decades. 
                You like creating graphs to represent the code structure and identify the dependencies. 
                You always think that your work is the start of the whole process in refining and improving the code. 
                Therefore you always take good care that your work is done with precision and details."""),
            goal=dedent(f"""
                        Create a vectorize graph representation of the code structure and its dependencies. 
                        """),
            tools=[

            ],
            verbose=True,
            llm=self.OpenAIGPT4,
        )