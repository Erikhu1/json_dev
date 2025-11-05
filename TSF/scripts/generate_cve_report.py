import json
import sys
from datetime import datetime, timezone

def generate_cve_report(codescanning_count, dependabot_count, total_count):
    """Generate a markdown report for CVE/security issues"""
    
    current_time = datetime.now(timezone.utc)
    
    print("# CVE and Security Issues Report\n")
    print(f"This report lists the current security vulnerabilities and issues for the json_dev repository.")
    print(f"The data is collected from GitHub's security APIs and updated regularly.\n")
    print(f"**Generated on:** {current_time.strftime('%Y-%m-%d %H:%M:%S UTC')}\n")
    
    print("## Summary\n")
    print("| Alert Type | Count |")
    print("|------------|-------|")
    print(f"| Code Scanning Alerts | {codescanning_count} |")
    print(f"| Dependabot Alerts | {dependabot_count} |")
    print(f"| **Total Open Issues** | **{total_count}** |\n")
    
    if total_count > 0:
        print("## Analysis\n")
        
        if codescanning_count > 0:
            print(f"### Code Scanning Alerts: {codescanning_count}")
            print("Code scanning alerts indicate potential security vulnerabilities found in the source code.")
            print("These should be reviewed and addressed promptly to maintain code security.\n")
        
        if dependabot_count > 0:
            print(f"### Dependabot Alerts: {dependabot_count}")
            print("Dependabot alerts indicate known security vulnerabilities in project dependencies.")
            print("Consider updating the affected dependencies to secure versions.\n")
        
    else:
        print("## Status: No Open Security Issues")
        print("\nNo open security issues were found in this repository.")
    
    print("---")
    print("*This report is automatically generated in the CI pipeline.*")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: generate_cve_report.py <codescanning_count> <dependabot_count> <total_count>", file=sys.stderr)
        sys.exit(1)
    
    try:
        codescanning_count = int(sys.argv[1])
        dependabot_count = int(sys.argv[2])
        total_count = int(sys.argv[3])
    except ValueError:
        print("Error: All arguments must be valid integers", file=sys.stderr)
        sys.exit(1)
    
    generate_cve_report(codescanning_count, dependabot_count, total_count)