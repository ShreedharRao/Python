username = input("Enter you username: ")
password = input("Enter your password: ")
passwordLength = len(password)
while passwordLength < 8:
    print("Password must be more than 8 characters long")
    password = input("Enter your password: ")
    passwordLength = len(password)

hiddenPassword = '*' * len(password)
print(f"Hello {username}, your password is {hiddenPassword}")