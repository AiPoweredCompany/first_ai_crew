from crewai import Task
from textwrap import dedent

from docutils.nodes import description

"""
Creating Tasks Cheat Sheet:
- Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve.
- Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
- Ensure tasks are descriptive, providing clear instructions and expected deliverables.

Goal:
- Analyse local repo code from a RAG using a vectorize database

Key Steps for Task Creation:
1. Identify the Desired Outcome: Define what success looks like for your project.
    - A vectorize database

2. Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
    - identify all the files containing code to analyze
    - save to vectorize database
    - Analyse code from the database: return a list of dependencies
    
3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.

4. Task Description Template:
  - Use this template as a guide to define each task in your CrewAI application. 
  - This template helps ensure that each task is clearly defined, actionable, and aligned with the specific goals of your project.

  Template:
  ---------
  def [task_name](self, agent, [parameters]):
      return Task(description=dedent(f'''
      **Task**: [Provide a concise name or summary of the task.]
      **Description**: [Detailed description of what the agent is expected to do, including actionable steps and expected outcomes. This should be clear and direct, outlining the specific actions required to complete the task.]

      **Parameters**: 
      - [Parameter 1]: [Description]
      - [Parameter 2]: [Description]
      ... [Add more parameters as needed.]

      **Note**: [Optional section for incentives or encouragement for high-quality work. This can include tips, additional context, or motivations to encourage agents to deliver their best work.]

      '''), agent=agent)

"""


class BackTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def retrieve_python_files_content(self, agent, local_repo):
        return Task(
            description=dedent(
                f"""
                    **Task**:  Retrieve all the files that contain python code from the local repo.
                    **Description**: Get all the files from the local repo and keep only the python files, 
                    these are the files to analyze.
                    **Parameters**: 
                    - Local repo: {local_repo}

                    **Note**: {self.__tip_section()}                
    """
            ),
            agent=agent,
            expected_output=f"""
            a list of python files content
    """
        )

    def save_data_to_database(self, agent):
        return Task(
            description=dedent(
                f"""
                        **Task**:  save or update all the coding files to the vectorized database.
                        **Description**: Save or update all the data into the vectorized database Chroma
                        **Note**: {self.__tip_section()}                
        """
            ),
            agent=agent,
            context=[self.identify_files_to_analyse()]
        )

    def code_analysis(self, agent):
        return Task(
            description=dedent(
                f"""
                    **Task**:  Analyse the code structure and its dependencies from the RAG
                    **Description**: Analyze the code structure and all its dependencies. This code is coming from the vectorized database 
                    All the dependencies between functions, classes, methods must be analysed in details to obtain 
                    a very precise and detailed result.
                    **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            context=[self.save_data_to_database()]
            expected_output=f"""
                a bullet list with the dependencies for each existing class aqnd then a bullet list with all dependencies for each function
        """
        )

