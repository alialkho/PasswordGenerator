import random

letters_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters_lowercase = 'abcdefghijklmnopqrstuvwxyz'
nums = '123456789'
chars = '!@#$%^&*'
passLength = int(input('Length of Password: '))
random_types = [letters_uppercase, letters_lowercase, nums, chars]
password = ''
for i in range(passLength):
    x = random.choice(random_types)
    password += f'{random.choice(x)}'

print(password)
