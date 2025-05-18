import requests

response = requests.get("https://api.github.com/users/Dheerajreddy9999/repos")

# print(response.json()[2])

my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']}\nProjectUrl: {project['html_url']}\nRepo Owner: {project['owner']['login']}\n")