import requests
import json

#get users

headers = {
    'HTTP-X-PARTNER-AUTH': 'site-name:api-key',
    'Content-Type' : 'application/json'
}

url = 'https://api.periscopedata.com/api/v2/users'

response = requests.get(url, headers=headers)

print(json.loads(response.text))

##################################################################

#get single user

headers = {
    'HTTP-X-PARTNER-AUTH': 'site-name:api-key',
    'Content-Type' : 'application/json'
}

url = 'https://api.periscopedata.com/api/v2/users/0000-test-1111-user-id'

response = requests.get(url, headers=headers)

print(json.loads(response.text))

#####################################################################

#get roles

headers = {
    'HTTP-X-PARTNER-AUTH': 'site-name:api-key',
    'Content-Type' : 'application/json'
}

url = 'https://api.periscopedata.com/api/v1/roles'

response = requests.get(url, headers=headers)

print(json.loads(response.text))

########################################################################

#get single role

headers = {
    'HTTP-X-PARTNER-AUTH': 'site-name:api-key',
    'Content-Type' : 'application/json'
}

url = 'https://api.periscopedata.com/api/v1/role/0000-test-1111-role-id'

response = requests.get(url, headers=headers)

print(json.loads(response.text))