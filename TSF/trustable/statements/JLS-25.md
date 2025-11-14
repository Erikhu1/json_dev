---
level: 1.1
normative: true
references:
        - type: web_content
          url: "https://scorecard.dev/viewer/?uri=github.com%2Fnlohmann%2Fjson"
          description: "OpenSSF Scorecard Report for nlohmann/json, where scores for 'Security-Policy' and 'Code-Review' reflect this statement."
        - type: project_website
          url: "https://github.com/nlohmann/json/blob/develop/.github/CONTRIBUTING.md"
          description: "Contribution Guidelines for nlohmann/json."
        - type: project_website
          url: "https://github.com/nlohmann/json/blob/develop/.github/SECURITY.md"
          description: "Security policy for nlohmann/json."
evidence:
        type: https_response_time
        configuration:
                target_seconds: 2
                urls:
                    - "https://github.com/nlohmann/json/blob/develop/.github/CONTRIBUTING.md"
                    - "https://github.com/nlohmann/json/blob/develop/.github/SECURITY.md"
score:
    Erikhu1: 0.8
---

Malicious code changes in nlohmann/json are mitigated by code reviews, adhering to the contribution guidelines and security policy specified by nlohmann/json.
