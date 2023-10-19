import hashlib

# Insecure Authentication
def insecure_authentication(password, stored_password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password == stored_password

# Password storage (insecure)
stored_password = "5d41402abc4b2a76b9719d911017c592"  # Hash of "password123"

# User input
user_password = input("Enter your password: ")

if insecure_authentication(user_password, stored_password):
    print("Authentication successful!")
else:
    print("Authentication failed!")

# In this example, the code stores and compares passwords using an insecure method. The passwords are stored as plain text or in a weakly hashed form, making them vulnerable to attack
#  It would also identify the use of the input() function for password entry, which is generally discouraged for secure applications.
