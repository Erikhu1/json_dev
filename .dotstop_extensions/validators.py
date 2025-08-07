from typing import Tuple
import os

def check_artifact_exists(artifact_name: str, artifact_dir: str) -> bool:
    """
    Check if the artifact for a specific workflow exists in the artifact directory.

    Parameters:
    - artifact_name: The unique identifier for the artifact (e.g., artifact_id).
    - artifact_dir: The directory where artifacts are expected.

    Returns:
    - True if the artifact exists, False otherwise.
    """
    artifact_path = os.path.join(artifact_dir, artifact_name)
    if os.path.exists(artifact_path) and os.path.isdir(artifact_path):
        print(f"✅ Artifact found: {artifact_name}")
        return True
    else:
        print(f"❌ Artifact missing: {artifact_name}")
        return False


def check_workflow_results(artifact_id: str, workflows: dict[str, str]) -> Tuple[float, list[str]]:
    """
    Check the successful creation of artifacts for workflows and calculate a score.

    Parameters:
    - artifact_id: The unique identifier for the artifacts (e.g., passed in by the workflow caller).
    - workflows: A dictionary of workflow names to their respective artifact directories.

    Returns:
    - A tuple containing:
      - The score (float), calculated as the ratio of successful artifacts to total workflows.
      - A list of workflows with missing artifacts.
    """
    total_workflows = len(workflows)
    successful_artifacts = 0
    missing_workflows = []

    for workflow_name, artifact_path in workflows.items():
        # Combine the artifact base path with the dynamic artifact ID (artifact_id)
        artifact_name = f"{workflow_name}-{artifact_id}"
        if check_artifact_exists(artifact_name, artifact_path):
            successful_artifacts += 1
        else:
            missing_workflows.append(workflow_name)

    # Calculate the score as the number of successful artifacts out of the total
    score = successful_artifacts / total_workflows if total_workflows > 0 else 0.0
    print(f"\nFinal Score: {score}")
    print(f"Workflows with missing artifacts: {missing_workflows}")
    return score, missing_workflows


def write_results_to_file(score: float, missing_workflows: list[str], output_file: str) -> None:
    """
    Write the validation results to a file.

    Parameters:
    - score: The calculated score.
    - missing_workflows: List of workflows with missing artifacts.
    - output_file: Path to the output file.
    """
    with open(output_file, "w") as f:
        f.write(f"Final Score: {score}\n")
        f.write(f"Workflows with missing artifacts: {missing_workflows}\n")


def main():
    """
    Entry point for running the validator from the command line.
    Expects environment variables or hardcoded values for demonstration.
    """
    # Example: Replace with actual logic to get these values
    artifact_id = os.environ.get("ARTIFACT_ID", "default_id")
    # Example workflow mapping: {"workflow_name": "artifact_dir"}
    workflows = {
        "workflow1": "artifacts",
        "workflow2": "artifacts",
        # Add more workflows as needed
    }
    score, missing = check_workflow_results(artifact_id, workflows)
    output_file = os.environ.get("VALIDATOR_OUTPUT_FILE", "validator_results.txt")
    write_results_to_file(score, missing, output_file)
    print(f"Results written to {output_file}")

if __name__ == "__main__":
    main()
