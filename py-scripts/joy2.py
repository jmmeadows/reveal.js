import boto3

client = boto3.client('translate')


response = client.translate_text(
    Text='learn and be curious',
    
    SourceLanguageCode='en',
    TargetLanguageCode='es'
)
print(response)