import os

folders = input("please enter the folders you waant to list files with colon \n").split(";")

for folder in folders:
    try:
      files = os.listdir(folder)
      print(f"files list in the folder: {folder}")
    except FileNotFoundError:
       print(f"Please Specify the correct folder: {folder}")
       continue
    except PermissionError:
       print(f"User does not have permission on the folder: {folder}")
    
    
    for file in files:
        print(file)
