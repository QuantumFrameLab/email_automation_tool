import json

users_file = "./data/users.json"

def register_member():
    username = str(input("Enter your username : "))
    password1 = input("Enter your password for tool : ")

    if len(password1) < 6 or len(password1) > 10:
        print("Password must be between 6 and 10 characters!")
        return
    password2 = input("Confirm your password : ")

    if password1 == password2:
        password = password1

        try:
            with open(users_file) as file:
                data = json.load(file)

        except(FileNotFoundError, json.JSONDecodeError):
            data = {"users" : []}

        if any( user["username"] == username for user in data["users"]):
            print("This username is already taken! Try different...")
            return
        
        data["users"].append({
            "username" : username,
            "password" : password
        })

        with open(users_file, "w") as file:
            json.dump(data, file, indent=4)
        
        print(f"{username} registered successfully!")
    
    else:
        print("Password not matched!")






        

