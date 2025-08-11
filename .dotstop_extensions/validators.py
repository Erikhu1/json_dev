from typing import TypeAlias
import os
import requests

yaml: TypeAlias = str | int | float | list["yaml"] | dict[str, "yaml"]

print(f"Current working directory in Python: {os.getcwd()}")

def check_artifact_exists(configuration: dict[str, yaml]) -> tuple[float, list[Exception | Warning]]:    
    print(os.getenv("GITHUB_SHA"))
    print (os.getenv("GITHUB_TOKEN"))
    print(os.getenv("GITHUB_RUN_ID"))
    print(os.getenv("GITHUB_REPOSITORY"))

    github_token = os.getenv("GITHUB_TOKEN")
    run_id = os.getenv("GITHUB_RUN_ID")
    repository = os.getenv("GITHUB_REPOSITORY")  
    score = 0.0

 # Ensure all required variables are available
    if not github_token or not run_id or not repository:
        raise RuntimeError("Missing required environment variables: GITHUB_TOKEN, GITHUB_RUN_ID, or GITHUB_REPOSITORY.")

    # GitHub API URL to list artifacts for the current workflow run
    url = f"https://api.github.com/repos/{repository}/actions/runs/{run_id}/artifacts"

    # Add authentication headers using the GitHub token
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github+json"
    }

    # Make the request to the GitHub API to fetch artifacts
    response = requests.get(url, headers=headers)

    # Check for a successful response
    if response.status_code != 200:
        raise RuntimeError(f"Failed to fetch artifacts: {response.status_code} - {response.text}")

    # Parse the JSON response
    data = response.json()
    artifacts = data.get("artifacts", [])

    # Extract artifact names
    artifact_names = [artifact["name"] for artifact in artifacts]

    # Print all items in artifact_names
    print("Listing all artifact names:")
    for name in artifact_names:
        print(f"- {name}")  # Print each artifact name
        
    for key,value in configuration.items():
        print(f"Checking workflow: {key},{value}")
        artifact_id = str(key)+"-"+os.getenv("GITHUB_SHA")

        if artifact_id in artifact_names:
            score = score + 1 / len(configuration)
            print(f"Artifact for workflow {key} found. Current cumulative score: {score}")
        else:
            print(f"Artifact for workflow {key} NOT found. Current cumulative score: {score}")
    return (score, [])


