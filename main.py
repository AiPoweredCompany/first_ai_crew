from crewai import Crew
from textwrap import dedent

from huggingface_hub import save_torch_state_dict
from numpy.lib.npyio import savez

from agents import BackDevAgents
from tasks import BackTasks




class ITCrew:
    def __init__(self, local_repo):
        self.local_repo = local_repo
        self.analysis = None
        self.graph = None

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = BackDevAgents()
        tasks = BackTasks()

        # Define your custom agents and tasks here
        code_analyst = agents.code_analyst_agent()

        # Custom tasks include agent name and variables as input
        retrieve_python_files_content = tasks.retrieve_python_files_content(
            code_analyst,
        )

        save_data_to_database = tasks.save_data_to_database(
            code_analyst,
        )

        analyze_code = tasks.code_analysis(
            code_analyst,
        )


        # Define your custom crew here
        crew = Crew(
            agents=[code_analyst,
                    ],
            tasks=[
                retrieve_python_files_content,
                save_data_to_database,
                analyze_code,
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
      What is the local repo you want to work on?
    """))

    IT_crew = ITCrew(repo)
    result = IT_crew.run()
    print("\n\n########################")
    print("## Here is you analysis ")
    print("########################\n")
    print(result)