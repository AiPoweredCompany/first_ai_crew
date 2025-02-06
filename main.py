from crewai import Crew
from textwrap import dedent
from agents import BackDevAgents
from tasks import BackTasks




class ITCrew:
    def __init__(self, remote_repo):
        self.remote_repo = remote_repo
        self.local_repo = None
        self.analysis = None
        self.graph = None

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = BackDevAgents()
        tasks = BackTasks()

        # Define your custom agents and tasks here
        code_analyst = agents.code_analyst_agent()

        # Custom tasks include agent name and variables as input
        fetch_remote_repo = tasks.fetch_repo(
            code_analyst,
            self.remote_repo
        )

        analyze_code = tasks.code_analysis(
            code_analyst,
            self.local_repo
        )

        create_vectorized_graph = tasks.create_vectorize_graph(
            code_analyst,
            self.analysis
        )

        create_image_from_graph = tasks.create_image_of_graph(
            code_analyst,
            self.graph
        )

        # Define your custom crew here
        crew = Crew(
            agents=[code_analyst,
                    ],
            tasks=[
                fetch_remote_repo,
                analyze_code,
                create_vectorized_graph,
                create_image_from_graph
            ],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to IT Crew")
    print('-------------------------------')
    repo = input(
        dedent("""
      What is the repo you want to work on?
    """))

    IT_crew = ITCrew(repo)
    result = IT_crew.run()
    print("\n\n########################")
    print("## Here is you analysis ")
    print("########################\n")
    print(result)