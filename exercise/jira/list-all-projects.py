import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://ksreddydheeraj.atlassian.net/rest/api/3/project"

API_TOKEN = ""
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