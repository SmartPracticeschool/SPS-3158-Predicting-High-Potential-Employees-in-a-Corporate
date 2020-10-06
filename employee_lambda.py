import os
import io
import boto3
import json
import csv

# grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    data = json.loads(json.dumps(event))
    payload = data['body']
    print('data',data)
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='text/csv',
                                       Body=payload)
    print('res',response)
    result = json.loads(response['Body'].read().decode())
    print('result',type(result))
    if(result == 0.0 ):
        prediction = 'Bad.'
    elif(result == 0.1):
        prediction = 'Not Satisfactory.'
    elif(result == 0.2):
        prediction = 'Satisfactory'
    elif(result==3.0):
        prediction = 'Good!'
    elif(result == 4.0):
        prediction = 'Great!'
    return prediction
