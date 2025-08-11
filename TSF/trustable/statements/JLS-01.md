---
level: 1.1
normative: true
evidence:
  type: "check_artifact_exists"
  configuration:
    check_amalgamation: "check_amalgamation"
    codeql-analysis: "codeql"
    dependency_review: "dependency_review"
    labeler: "labeler"
    test_trudag_extensions: "test_trudag_extensions"
    ubuntu: "ubuntu"

---

The JSON-library project CI executes on each pull request (opened, reopened, synchronized) the integration test suite, and failures in these runs are investigated by contributors.
