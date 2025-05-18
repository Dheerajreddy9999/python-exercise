def update_server_conf(file_path, key, value):
    
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:

            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)



config_file = 'D:/gitrepos/python-exercise/exercise/file-operations/server.conf'

key_to_update = 'MAX_CONNECTIONS'

new_value = '900000'

update_server_conf(config_file, key_to_update,new_value)