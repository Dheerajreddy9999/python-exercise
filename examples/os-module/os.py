import os

current_directory=os.getcwd()
full_path=os.path.join(current_directory,"python-exercise")

if os.path.exists(full_path):
    print(f"directory {full_path} exists")




home_dir=os.path.expanduser("~/")

full_path=os.path.join(home_dir,"Documents")

if os.path.exists(full_path):
    print(f"directory {full_path} exists")




file_path=os.path.abspath(__file__)
parent_path=os.path.dirname(file_path)

full_path=os.path.join(parent_path,"examples")

print(f"checking {full_path}")

if os.path.exists(full_path):
    print(f"file exists {full_path}")




list_dir=[os.getcwd(), os.path.expanduser("~/"), os.path.abspath(__file__)]

for path in list_dir:
    if path is not None:
        file_path=os.path.join(path,"python-exercise")

        if os.path.exists(file_path):
            print(f"path {file_path} exists")
        else:
            print(f"path {file_path} does not exists in the system")



import os

d=os.getcwd()

print(d)

os.chdir("C:/")

d=os.getcwd()

print(d)



d=os.environ.get("hj")
print(d)

os.environ["hj"]="env1"

d=os.environ.get("hj")
print(d)