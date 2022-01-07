import json
import uuid

GET_RAW_PATH = "/getPerson"
CREATE_RAW_PATH = "/createPerson"

def lambda_handler(event, context):
    print(event)
    if event['rawPath'] == GET_RAW_PATH:
        print('Received getPerson request')
        personId = event['queryStringParameters']['personId']
        print("with param personId=" + personId)
        return { "personId": personId, "firstName": "Suresh", "lastName": "Nikuliya", "email": "myEmail@gmail.com" }
    elif event['rawPath'] == CREATE_RAW_PATH:
        print('Received createPerson request')
        decodedBody = json.loads(event['body'])
        firstName = decodedBody['firstName']
        print('with param firstName=' + firstName)
        return { "personId": str(uuid.uuid1())}