from crewai import Task
from textwrap import dedent

from docutils.nodes import description

"""
Creating Tasks Cheat Sheet:
- Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve.
- Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
- Ensure tasks are descriptive, providing clear instructions and expected deliverables.

Goal:
- Create a vectorize graph and the equivalent JSON file of the code structure and its dependencies related to the given repo.

Key Steps for Task Creation:
1. Identify the Desired Outcome: Define what success looks like for your project.
    - A JSON file with the code structure and its dependencies.
    - The image (png format) of the corresponding vectorize graph 

2. Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
    - Fetch the repo: connect to the remote repo and get a clone in local
    - Code analysis: analyse the code structure and its dependencies of the local repo
    - Create vectorize graph: Generate the vectorize graph related to the code structure
    - Create image of the graph: Generate a png image of this vectorize graph and save it in the actual repo

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

    def fetch_repo(self, agent, remote_repo):
        return Task(
            description=dedent(
                f"""
            **Task**: Fetch the remote repo
            **Description**: Fetch the remote repo to clone it in local. 
            The clone is created in a new local repo with the same name as the remote one.

            **Parameters**: 
            - Remote repo: {remote_repo}

            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
        )

    def code_analysis(self, agent, local_repo):
        return Task(
            description=dedent(
                f"""
                    **Task**:  Analyse the code structure and its dependencies for the local repo
                    **Description**: Analyze the code structure of the local repo and all its dependencies. 
                    All the dependencies between functions, classes, methods must be analysed in details to obtain 
                    a very precise and detailed result.

                    **Parameters**: 
                    - Local repo: {local_repo}

                    **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
        )

    def create_vectorize_graph(self, agent, analysis):
        return Task(
            description=dedent(
                f"""
                    **Task**:  Create a vectorize graph of the analysis
                    **Description**: Use the analysis to generate a detailed and precise vectorize graph of it.

                    **Parameters**: 
                    - Analysis: {analysis}

                    **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
        )

    def create_image_of_graph(self, agent, vectorized_graph):
        return Task(
            description=dedent(
                f"""
                    **Task**: Create an image of the vectorized graph
                    **Description**: Create a png image of the whole vectorized graph.
                    
                    **Parameters**:
                    - Vectorized Graph: {vectorized_graph}
                    
                    **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
        )