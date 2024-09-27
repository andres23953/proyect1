import boto3
from google.cloud import storage

# AWS S3
s3 = boto3.client('s3')
try:
    s3.create_bucket(Bucket='mi-bucket')
except Exception as e:
    print(f'Error creando bucket en S3: {e}')

# GCP Cloud Storage
gcs_client = storage.Client()
try:
    gcs_client.bucket('mi-bucket-gcp').create()
except Exception as e:
    print(f'Error creando bucket en GCP: {e}')
