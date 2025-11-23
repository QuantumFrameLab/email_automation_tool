import json

def delete_email():
    file_path = "./data/emails.json"

    while True:
        email_to_delete = input("Enter email to Delete : ")

        if email_to_delete.lower() in ["b", "0", "back"]:
            print("reurturning to menu...")
            return
        
        if email_to_delete.lower().endswith("@gmail.com"):
            try:
                with open(file_path) as file:
                    emails = json.load(file)
            except(FileNotFoundError, json.JSONDecodeError):
                emails = []
            
            if email_to_delete in emails:
                emails.remove(email_to_delete)

                with open(file_path, "w") as file:
                    json.dump(emails, file, indent=4)
                print(f"{email_to_delete} deleted successfully.")
            
            else: 
                print(f"{email_to_delete} not Found...")

