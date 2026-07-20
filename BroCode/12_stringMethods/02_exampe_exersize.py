# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")



if len(username) > 12: # checks the length of the username
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1: #  -1 if no spaces are found
    print("Your username can't contain spaces")
elif not username.isalpha(): # checks if the username has anything thats not a letter
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")