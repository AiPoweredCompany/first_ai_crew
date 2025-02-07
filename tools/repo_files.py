import os

from langchain.tools import tool


class RepoTools:

    def retrieve_python_files(repo_path: str) -> list:
        """
        Retrieve all Python files in the given repository path.
        :param repo_path: Path to the root of the repository.
        :return: List of Python file paths relative to the repository root.
        """
        python_files = []

        for root, _, files in os.walk(repo_path):
            for file in files:
                if file.endswith(".py"):
                    relative_path = os.path.relpath(os.path.join(root, file), repo_path)
                    python_files.append(relative_path)
        print("python_files = ", python_files)
        print("python files found = ", len(python_files))
        return python_files

    def get_file_content(file_path: str) -> str:
        """
        Read and return the content of a Python file.

        :param file_path: Path to the Python file.
        :return: Content of the file as a string.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            return f"Error reading file {file_path}: {e}"

    @tool("return all python files content from the repo")
    def retrieve_python_files_content(self, repo_path):
        result = []
        files = self.retrieve_python_files(repo_path)
        for file in files:
            result.append(self.get_file_content(file))
            print(f"{len(result)} content file(s) retrieved")
        return result