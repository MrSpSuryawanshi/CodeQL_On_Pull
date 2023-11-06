import os

# Simulate data leakage by printing sensitive information
def log_sensitive_data(username, password):
    print(f"User: {username}, Password: {password}")

if __name__ == "__main__":
    username = "john_doe"
    password = "s3cr3tp@ssw0rd"
    
    # Simulate authentication and data handling
    if username == "admin" and password == "admin123":
        print("Admin login successful.")
    else:
        print("User login successful.")
    
    log_sensitive_data(username, password)


# The log_sensitive_data function is used to log sensitive information (in this case, a username and password) directly to the console.
