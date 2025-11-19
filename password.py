password = input("Enter password: ")

# Check length
if len(password) < 6 or len(password) > 16:
    print("Invalid password (length must be 6 to 16 characters)")
else:
    lower = False
    upper = False
    digit = False
    special = False

    for ch in password:
        if ch >= 'a' and ch <= 'z':
            lower = True
        elif ch >= 'A' and ch <= 'Z':
            upper = True
        elif ch >= '0' and ch <= '9':
            digit = True
        elif ch in "@#$":
            special = True

    if lower and upper and digit and special:
        print("Password is valid")
    else:
        print("Invalid password")
