import requests
import json
from modules.aws_inventory import aws_inventory
from modules.azure_inventory import azure_inventory

MODEL = "qwen2.5:1.5b"

def ai_audit():
    print("Collecting AWS and Azure data...")

    data = {
        "aws": aws_inventory(),
        "azure": azure_inventory()
    }

    prompt = f"""
You are a senior multi-cloud security and cost optimization engineer.

Analyze this AWS and Azure inventory.

Provide:
1. Security observations
2. Cost optimization suggestions
3. Architecture recommendations
4. Top 5 priority actions

Cloud Data:
{json.dumps(data, indent=2)}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=180
    )

    result = response.json()
    report = result.get("response", str(result))

    print("\n===== MULTI-CLOUD AI AUDIT REPORT =====\n")
    print(report)

    with open("reports/multi-cloud-audit-report.md", "w") as f:
        f.write("# Multi-Cloud AI Audit Report\n\n")
        f.write(report)
