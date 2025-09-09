import yaml

file_path = 'D:\gitrepos\python-exercise\examples\pyYaml\example-3\employees.yaml'

with open(file_path, 'r') as file:
    employees_data = yaml.safe_load(file)

for employee in employees_data['employees']:
    print(f"Employee: {employee['name']}, age: {employee['age']}")
