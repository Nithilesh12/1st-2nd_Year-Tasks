import hashlib

def hash_password(password):
    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def register(username, password):
    # Hash the password
    hashed_password = hash_password(password)

    # Check if the user already exists
    with open('users.txt', 'r') as file:
        for line in file:
            if line.strip().split(',')[0] == username:
                print("User already exists. Please choose a different username.")
                return

    # Save the user information to the text file
    with open('users.txt', 'a') as file:
        file.write(f"{username},{hashed_password}\n")
        print("Registration successful.")

def login(username, password):
    # Hash the password
    hashed_password = hash_password(password)

    # Check if the user exists and the password is correct
    with open('users.txt', 'r') as file:
        for line in file:
            stored_username, stored_hashed_password = line.strip().split(',')
            if stored_username == username and stored_hashed_password == hashed_password:
                print("Login successful.")
                return

    print("Invalid username or password.")

def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            register(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            login(username, password)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()