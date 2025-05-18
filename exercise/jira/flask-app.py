import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask

app = Flask(__name__)

@app.route('/jira', methods=['POST'])
def createjira():
    url = "https://ksreddydheeraj.atlassian.net/rest/api/3/issue"

    API_TOKEN = ""

    auth = HTTPBasicAuth("ksreddy.dheeraj@gmail.com", API_TOKEN)

    headers = {
      "Accept": "application/json",
      "Content-Type": "application/json"
    }

    payload = json.dumps( {
      "fields": {
        "description": {
          "content": [
            {
              "content": [
                {
                  "text": "My First ticket",
                  "type": "text"
                }
              ],
              "type": "paragraph"
            }
          ],
          "type": "doc",
          "version": 1
        },
        "summary": "Github issue template",
        "issuetype": {
          "id": "10003"
        },
        "project": {
          "key": "P1"
        },
      },
      "update": {}
     } )

    response = requests.request(
       "POST",
       url,
       data=payload,
       headers=headers,
       auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))


if __name__ == '__main__':
    app.run(host="0.0.0.0")

    