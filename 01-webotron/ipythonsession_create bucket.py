# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print (bucket)

new_bucket1 = s3.create_bucket(Bucket='mohan-03',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    })
