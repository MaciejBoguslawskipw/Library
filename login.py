import logging

logging.basicConfig(filename="operations.log", level=logging.INFO)

class User:
    def __init__(self, username, email, role):
        self.username = username
        self.email = email
        self.role = role

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)
        logging.info(f"Added user: {user.username}")

    def remove_user(self, username):
        self.users = [u for u in self.users if u.username != username]
        logging.info(f"Removed user: {username}")

    def show_users(self):
        for user in self.users:
            print(f"{user.username}, {user.email}, {user.role}")

def main():
    manager = UserManager()
    while True:
        print("1. Add user")
        print("2. Remove user")
        print("3. Show users")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            email = input("Enter email: ")
            role = input("Enter role: ")
            manager.add_user(User(username, email, role))
        elif choice == "2":
            username = input("Enter username to remove: ")
            manager.remove_user(username)
        elif choice == "3":
            manager.show_users()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
