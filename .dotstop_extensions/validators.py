from typing import TypeAlias
import os

yaml: TypeAlias = str | int | float | list["yaml"] | dict[str, "yaml"]

def check_artifact_exists(configuration: dict[str, yaml]) -> tuple[float, list[Exception | Warning]]:
    workflow_name = configuration.get("workflow_name")
    artifact_id = workflow_name+os.getenv("GITHUB_SHA")

    if check_name_in_file(artifact_id, "all_artifacts.txt"):
        score = 0.8
    else:
        score = 0.2
    print(f"Test execution check for '{artifact_id}' assigns the score: {score}")
    return (score, [])


def check_name_in_file(name_to_check, file_path):
    try:
        with open(file_path, 'r') as file:
            # Read all lines in the file
            contents = file.read()
            
            # Check if the name exists in the file (case-sensitive match)
            if name_to_check in contents:
                return True
            else:
                return False
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return False