import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

if response.status_code == 200:

    pull_requests = response.json()

    pr_creators = {}

    for pull in pull_requests:
        creator = pull['user']['login']
        
        if creator in pr_creators:
            pr_creators[creator] = pr_creators[creator] + 1
        else:
            pr_creators[creator] = 1
     
    print("pr creators and their counts")
    for creator,count in pr_creators.items():
        print(f"{creator}: {count} PR(s)")

else:
    print(f"Failed to fetch data. Status code: {response.status_code}")