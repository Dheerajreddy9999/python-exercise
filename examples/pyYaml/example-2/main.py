import yaml

file_path = 'D:/gitrepos/python-exercise/examples/pyYaml/example-2/config.yaml'

with open(file_path, 'r') as file:
    config_file = yaml.safe_load(file)

print(f"Config file: {config_file}")

config_file['server']['port'] = 9000
config_file['database']['name'] = "dheeraj"

with open(file_path , 'w') as file:
    yaml.dump(config_file,file)

print(f"Updated config file: {config_file}")