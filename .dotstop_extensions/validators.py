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
