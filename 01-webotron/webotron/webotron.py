
import boto3
import sys
import click
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
@click.group()
def cli():
    "webton deploys web sites to AWS"
    pass

@cli.command('list-buckets')
def list_buckets():
    "List all S3 bckets"
    for bucket in s3.buckets.all():
        print (bucket)
@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "List all Bucket objects"
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)
if __name__=='__main__':
    cli()
