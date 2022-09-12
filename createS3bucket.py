import boto3

sess= boto3.Session(region_name='us-east-2')
s3client = sess.client('s3')
bucket_name='big-thing-happen-big1'
s3_location={
    'LocationConstraint': 'us-east-2'
}
try:
    s3client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=s3_location)
    print('Bucket created')
except s3client.BucketAlreadyExists as err:
    print('Error Mesaage: {}'.format(err.response['Error']['Message']))
