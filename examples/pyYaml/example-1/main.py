import yaml

file_path = 'D:/gitrepos/python-exercise/examples/pyYaml/example-1/user.yaml'
updated_path = 'D:/gitrepos/python-exercise/examples/pyYaml/example-1/user_updated.yaml'


with open(file_path, 'r') as file:
    user_data = yaml.safe_load(file)

print("Loaded Ymal file:",user_data)

updated_yaml = {'name': 'Dheeraj', 'age': 26, 'is_developer': True}

with open(updated_path, 'w') as file:
    yaml.dump(updated_yaml,file)


with open(updated_path, 'r') as file:
   update_data=yaml.safe_load(file)

print(f"Updated Yaml File: {updated_yaml}")