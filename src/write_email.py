import subprocess
import json
from register_user import register_member

def write_email():
    member_temp_path = "./data/templates/member_template.txt"
    owner_temp_path = "./data/templates/owner_template.txt"
    temp_file = "./data/templates/temp.txt"
    users_file = "./data/users.json"

    username = str(input("Enter your username : "))
    password = input("Enter your password : ")

    try:
        with open(users_file) as file:
            data = json.load(file)

    except(FileNotFoundError, json.JSONDecodeError):
        print("NO user found... Make one")
        data = {"users" : []}
        register_member()
    
    if any(user["username"] == username and user["password"] == password for user in data["users"]):
        if username == "kamran":
            with open(owner_temp_path) as file:
                temp_content = file.read()
              
        else:
            with open(member_temp_path) as file:
                temp_content = file.read()

    else:
        print("Something went wrong...")
        return
    
    with open(temp_file, "w") as file:
        file.write(temp_content)
    
    subprocess.call(["notepad.exe", temp_file])

    print("Your email has been saved in temp.txt")

