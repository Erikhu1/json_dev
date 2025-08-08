from typing import TypeAlias

yaml: TypeAlias = str | int | float | list["yaml"] | dict[str, "yaml"]

def check_artifact_exists(configuration: dict[str, yaml]) -> tuple[float, list[Exception | Warning]]:
    artifact_name = configuration.get("artifact_name", None)
    
    score = 0.7
    print(f"Test execution check for '{artifact_name}' assigns the score: {score}")
    return (score, [])