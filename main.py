from modules.aws_inventory import aws_inventory
from modules.azure_inventory import azure_inventory
from modules.ai_auditor import ai_audit
from modules.cost_optimizer import cost_optimizer
from modules.terraform_generator import terraform_generator

while True:
    print("""
====================================
 MULTI-CLOUD AI OPS PLATFORM
====================================

1. AWS Inventory
2. Azure Inventory
3. AI Security Audit
4. Cost Optimizer
5. AI Terraform Generator
6. Exit
""")

    choice = input("Select option: ")

    if choice == "1":
        aws_inventory()
    elif choice == "2":
        azure_inventory()
    elif choice == "3":
        ai_audit()
    elif choice == "4":
        cost_optimizer()
    elif choice == "5":
        terraform_generator()
    elif choice == "6":
        break
    else:
        print("Invalid option")
