import boto3

sess= boto3.Session(region_name='us-east-2')
s3client = sess.client('s3')
bucket_name='big-thing-happen-big1'
s3_location={
    'LocationConstraint': 'us-east-2'
}

def bucket_exist(bucket_name):
    s3 = boto3.resource('s3')
    return s3.bucket(bucket_name) in s3.bucket.all()

if bucket_exist(bucket_name):
    print('the bucket already exist')
    #Do nothing

else:
    #create bucket
    s3client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=s3_location)
    print('the bucket created')


#     s3client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=s3_location)
# except s3client.BucketAlreadyExists as err:
#     print('Error Mesaage: {}'.format(err.response['Error']['Message']))
