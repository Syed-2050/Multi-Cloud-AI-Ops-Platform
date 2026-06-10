import subprocess
import json

def run_az(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        return []
    return json.loads(result.stdout) if result.stdout.strip() else []

def azure_inventory():
    data = {
        "resource_groups": run_az(["az", "group", "list", "-o", "json"]),
        "virtual_machines": run_az(["az", "vm", "list", "-o", "json"]),
        "storage_accounts": run_az(["az", "storage", "account", "list", "-o", "json"]),
        "vnets": run_az(["az", "network", "vnet", "list", "-o", "json"]),
        "nsgs": run_az(["az", "network", "nsg", "list", "-o", "json"])
    }

    print(json.dumps(data, indent=2))
    return data
