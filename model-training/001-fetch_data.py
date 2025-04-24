import os
import boto3
import pandas as pd
from io import StringIO

if __name__ == "__main__":
    print("📥 Fetching data from S3...")

    s3_client = boto3.client(
        "s3",
        endpoint_url=os.environ.get("AWS_S3_ENDPOINT"),
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
    )

    response = s3_client.get_object(
        Bucket=os.environ["AWS_S3_BUCKET"],
        Key="data/diabetes.csv"
    )

    data = pd.read_csv(StringIO(response["Body"].read().decode("utf-8")))
    data.to_csv("diabetes.csv", index=False)
    print("✅ Data saved to diabetes.csv")

