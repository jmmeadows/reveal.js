import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')



# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
    
    
    
    # Upload a new file
data = open('viola.jpg', 'rb')
s3.Bucket('jonetta.cloud').put_object(Key='viola.jpg', Body=data)


joy = boto3.client('rekognition')


response = joy.recognize_celebrities(
    Image={
        #'Bytes': b'bytes',
        'S3Object': {
            'Bucket': 'jonetta.cloud',
            'Name': 'viola.jpg',
            #'Version': 'string'
        }
    }
)
print(response)