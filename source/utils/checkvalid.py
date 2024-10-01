def check_username(user: str) -> bool:
    """
    Check if the username has more than 6 characters.
    :param user: The username to check.
    :return: True if the username is valid, False otherwise.
    """
    return len(user) > 6

def check_pw(pw: str) -> bool:
    """
    Check if the password has more than 6 characters.
    Additional password validation logic can be added here.
    :param pw: The password to check.
    :return: True if the password is valid, False otherwise.
    """
    return len(pw) > 6

# Example usage
# username = "myuser1"
# password = "mypassword"

# if check_user(username) and check_pw(password):
#     print("Login successful.")
# else:
#     print("Invalid username or password.")
