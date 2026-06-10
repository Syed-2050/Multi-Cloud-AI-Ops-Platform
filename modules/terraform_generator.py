import requests

MODEL = "qwen2.5:1.5b"

def terraform_generator():
    user_request = input("Describe infrastructure to generate Terraform: ")

    prompt = f"""
Generate valid Terraform code only.

Requirements:
{user_request}

Rules:
- Output Terraform only
- No explanations
- No markdown
- No comments
- Complete code
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
    code = result.get("response", str(result))

    with open("terraform/main.tf", "w") as f:
        f.write(code)

    print("\nTerraform saved to terraform/main.tf\n")
    print(code)
