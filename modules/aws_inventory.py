import boto3
import json

def aws_inventory():
    ec2 = boto3.client("ec2")
    s3 = boto3.client("s3")
    iam = boto3.client("iam")

    data = {
        "ec2_instances": [],
        "s3_buckets": [],
        "iam_users": []
    }

    for r in ec2.describe_instances()["Reservations"]:
        for i in r["Instances"]:
            data["ec2_instances"].append({
                "id": i["InstanceId"],
                "state": i["State"]["Name"],
                "type": i["InstanceType"]
            })

    for b in s3.list_buckets()["Buckets"]:
        data["s3_buckets"].append(b["Name"])

    for u in iam.list_users()["Users"]:
        data["iam_users"].append(u["UserName"])

    print(json.dumps(data, indent=2))
    return data
