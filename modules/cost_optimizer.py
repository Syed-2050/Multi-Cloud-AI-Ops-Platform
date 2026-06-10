import boto3

def cost_optimizer():
    ec2 = boto3.client("ec2")
    findings = []

    instances = ec2.describe_instances()
    for r in instances["Reservations"]:
        for i in r["Instances"]:
            if i["State"]["Name"] == "stopped":
                findings.append(f"Stopped EC2 instance: {i['InstanceId']}")

    volumes = ec2.describe_volumes()
    for v in volumes["Volumes"]:
        if len(v["Attachments"]) == 0:
            findings.append(f"Unattached EBS volume: {v['VolumeId']}")

    print("\n===== COST OPTIMIZATION REPORT =====\n")

    if findings:
        for item in findings:
            print("-", item)
    else:
        print("No obvious unused AWS resources found.")
