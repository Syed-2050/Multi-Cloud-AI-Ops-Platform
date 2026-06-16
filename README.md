# Multi-Cloud AI Ops Platform

An AI-powered multi-cloud operations platform that inventories AWS and Azure resources, audits security, optimises costs, and generates Terraform code — all using a local AI model with no paid API costs.

## Live Portfolio
🌐 https://d2rmjt7abyfd3o.cloudfront.net

---

## What It Does

| Module | Description |
|---|---|
| AWS Inventory | Scans EC2, S3, IAM resources |
| Azure Inventory | Scans VMs, Storage, NSGs, VNets |
| AI Security Auditor | Multi-cloud security and cost report |
| Cost Optimizer | Finds stopped EC2s and unattached volumes |
| Terraform Generator | Generates IaC from plain English description |

---

## Architecture

AWS Account -----+
|---> Python Automation ---> Ollama Local AI (Qwen2.5)
Azure Account ----+                                    |
v
Multi-Cloud Audit Report
|
v
Terraform Code Generator


---

## Project Structure

multi-cloud-ai-ops-platform/
|-- main.py
|-- requirements.txt
|-- README.md
|-- .gitignore
|-- modules/
|   |-- aws_inventory.py
|   |-- azure_inventory.py
|   |-- ai_auditor.py
|   |-- cost_optimizer.py
|   -- terraform_generator.py |-- terraform/ |   -- main.tf
-- reports/     -- sample-report.md

---

## Tools and Technologies

| Category | Tools |
|---|---|
| Cloud | AWS, Microsoft Azure |
| Language | Python 3 |
| AWS SDK | Boto3 |
| Azure | Azure CLI |
| Local AI | Ollama, Qwen2.5 1.5b |
| IaC | Terraform |
| Version Control | Git, GitHub |
| OS | Linux Ubuntu, WSL |

---

## How to Run

### Prerequisites
- AWS CLI configured with IAM credentials
- Azure CLI logged in
- Ollama installed and running
- Python 3 installed

### Setup

```bash
git clone https://github.com/Syed-2050/multi-cloud-ai-ops-platform.git
cd multi-cloud-ai-ops-platform

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

ollama run qwen2.5:1.5b

aws sts get-caller-identity
az account show --output table

python main.py
```

---

## Menu Options

====================================
MULTI-CLOUD AI OPS PLATFORM

1.AWS Inventory
2.Azure Inventory
3.AI Security Audit
4.Cost Optimizer
5.AI Terraform Generator
6.Exit

---

## Sample Terraform Output

Input: Create a VPC with public and private subnets on AWS

Output: Complete Terraform HCL code with resource blocks, variables and outputs

---

## Skills Demonstrated

- Multi-cloud infrastructure management (AWS + Azure)
- Python automation with Boto3 and Azure CLI
- Local AI integration using Ollama
- Infrastructure as Code with Terraform
- Cloud security auditing and cost optimisation
- Linux administration and CLI workflows
- Git version control and GitHub

---


## Author

**Syed Arif Ali**
Cloud & DevOps Engineer | AWS | Azure | Python | AI Automation

- Email: Syedarif1907@gmail.com
- LinkedIn: https://linkedin.com/in/syed-arif-a-a13782407
- GitHub: https://github.com/Syed-2050
- Portfolio: https://d2rmjt7abyfd3o.cloudfront.net
