
# import sys
# import boto3

# sess= boto3.Session(region_name='us-east-2')
# s3client = sess.client('s3')
# # command line argument for bucket name
# bucket_name = sys.argv[1]

# s3_location={
#     'LocationConstraint': 'us-east-2'
# }
# ################# This section is for aws copepipeline
# import sys
# import boto3

# sess= boto3.Session(region_name='us-east-2')
# s3client = sess.client('s3')
# # command line argument for bucket name
# bucket_name = sys.argv[1]

# s3_location={
#    'LocationConstraint': 'us-east-2'
# }

# def bucket_exists(bucket_name):
#  s3 = boto3.resource('s3')
#  return s3.Bucket(bucket_name) in s3.buckets.all()

# if bucket_exists(bucket_name):
#  print('the bucket already exists!')
#   # Do nothing
# else:
#   # create bucket
#  s3client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=s3_location)
#  print('the bucket created')


# #######################The above is for aws codepipeline



 #!/bin/bash/env python3
import boto3

sess= boto3.Session(region_name='us-east-1')
s3client = sess.client('s3')
bucket_name='good-trying'
s3_location={
    'LocationConstraint': 'us-east-1'
}

def bucket_exists(bucket_name):
  s3 = boto3.resource('s3')
  return s3.Bucket(bucket_name) in s3.buckets.all()

if bucket_exists(bucket_name):
  print('the bucket already exists!')
   #Do nothing
else:
   #create bucket
  s3client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=s3_location)
  print('the bucket created')






# #!/bin/bash/env python3
# import boto3

# sess= boto3.Session(region_name='us-east-2')
# s3client = sess.client('s3')
# bucket_name='good-trying3'
# s3_location={
#     'LocationConstraint': 'us-east-2'
# }

# def bucket_exists(bucket_name):
#   s3 = boto3.resource('s3')
#   return s3.Bucket(bucket_name) in s3.buckets.all()

# if bucket_exists(bucket_name):
#   print('the bucket already exists!')
#   #Do nothing
# else:
#   #create bucket
#   s3client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=s3_location)
#   print('the bucket created')

#     s3client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=s3_location)
# except s3client.BucketAlreadyExists as err:
#     print('Error Mesaage: {}'.format(err.response['Error']['Message']))
