#!/usr/bin/python
from ansible.module_utils.basic import *
import boto3

iam = boto3.client('iam')

# List access keys through the pagination interface.
paginator = iam.get_paginator('list_access_keys')
for response in paginator.paginate(UserName='user_name'):
    print(response)

last_used_Access_key = response['AccessKeyMetadata'][0]['AccessKeyId']
print(last_used_Access_key)

#create access key
response = iam.create_access_key(
    UserName='user_name'
)
#new_access_key_Id = response['AccessKeyId']
print(response)

new_access_key_Id = response['AccessKey']['AccessKeyId']
new_secreat_key = response['AccessKey']['SecretAccessKey']
Key_dict = {new_access_key_Id: new_secreat_key }
print(Key_dict)
