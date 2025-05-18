import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://ksreddydheeraj.atlassian.net/rest/api/3/project"

API_TOKEN = "ATATT3xFfGF0tERAou7-WFYbEZcf-RNprcOyRnKUqADnsQBZPKXg2w2zsUIa73eiZGQVRIL8EDOh_6M1k3RZP0CjMpduGoQl4WLNglc7IKyQTj7un7JM7vvyYw_iEfyf1G5seWdM6bZN-0PbVC6CTBJOT4MYvQp0N5fK14Q2zsF2o3HXbGwgiNU=89E28883"

auth = HTTPBasicAuth("ksreddy.dheeraj@gmail.com",API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)


for project in json.loads(response.text):
    print(project['name'])