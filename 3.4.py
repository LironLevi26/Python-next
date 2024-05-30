import string

class UsernameContainsIllegalCharacter(Exception):
    """Exception raised when the username contains an illegal character."""

    def __init__(self, char, index):
        """
        Initialize with the illegal character and its index.
        :param char: The illegal character.
        :param index: The index of the illegal character in the username.
        """
        self.char = char
        self.index = index

    def __str__(self):
        return f"The username contains an illegal character '{self.char}' at index {self.position}"

class UsernameTooShort(Exception):
    """Exception raised when the username is too short."""

    def __str__(self):
        return "The username is too short"

class UsernameTooLong(Exception):
    """Exception raised when the username is too long."""

    def __str__(self):
        return "The username is too long"

class PasswordMissingCharacter(Exception):
    """Exception raised when the password is missing a required character."""

    def __str__(self):
        return "The password is missing a character"

class PasswordMissingUppercase(PasswordMissingCharacter):
    """Exception raised when the password is missing an uppercase letter."""

    def __str__(self):
        return super().__str__() + " (Uppercase)"

class PasswordMissingLowercase(PasswordMissingCharacter):
    """Exception raised when the password is missing a lowercase letter."""

    def __str__(self):
        return super().__str__() + " (Lowercase)"

class PasswordMissingDigit(PasswordMissingCharacter):
    """Exception raised when the password is missing a digit."""

    def __str__(self):
        return super().__str__() + " (Digit)"

class PasswordMissingSpecial(PasswordMissingCharacter):
    """Exception raised when the password is missing a special character."""

    def __str__(self):
        return super().__str__() + " (Special)"

class PasswordTooShort(Exception):
    """Exception raised when the password is too short."""

    def __str__(self):
        return "The password is too short (less than 8 characters)"

class PasswordTooLong(Exception):
    """Exception raised when the password is too long."""

    def __str__(self):
        return "The password is too long (more than 40 characters)"

def check_input(username, password):
    """
    Check if the given username and password are valid based on defined rules.
    :param username: The username to check.
    :param password: The password to check.
    """
    if not (3 <= len(username) <= 16):
        if len(username) < 3:
            raise UsernameTooShort()
        else:
            raise UsernameTooLong()

    for i, char in enumerate(username):
        if char not in string.ascii_letters + string.digits + '_':
            raise UsernameContainsIllegalCharacter(char, i)

    if not (8 <= len(password) <= 40):
        if len(password) < 8:
            raise PasswordTooShort()
        else:
            raise PasswordTooLong()

    if not any(char.isupper() for char in password):
        raise PasswordMissingUppercase()
    if not any(char.islower() for char in password):
        raise PasswordMissingLowercase()
    if not any(char.isdigit() for char in password):
        raise PasswordMissingDigit()
    if not any(char in string.punctuation for char in password):
        raise PasswordMissingSpecial()

    print("OK")


def main():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            check_input(username, password)
            break
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()
