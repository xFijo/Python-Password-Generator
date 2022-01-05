import string
import random
import crayons
import os
import time

def clear_py():
    os.system('cls')

clear_py()

lines = '-------------------------------------------------------------'

characters = list(string.ascii_letters + string.digits + "!£$%^&*()_+")

def generate_random_password():
    length = int(input(crayons.cyan("Enter password length : ")))
    print(crayons.green(f'Passowrd Generating! Digits: {length}'))
    os.system('Title Password Generating.')
    time.sleep(1.5)
    random.shuffle(characters)
    password = []
    for i in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    os.system('Title Password Generated!')
    print(crayons.green('Password Generated'))
    print('\n')
    print(crayons.red(lines))
    print('\n')
    print(crayons.green("" .join(password)))
    print('\n')
    print(crayons.red(lines))
    print('\n')

generate_random_password()