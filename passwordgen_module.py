import string
import random

def passwordgen():
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for x in range(random.randrange(8, 16)))
    return password

def main():
    passwordgen()

if __name__ == '__main__':
    main()

print("Your password is: ", passwordgen())