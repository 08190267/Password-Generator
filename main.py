import random
import string

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_chars = letters + digits + symbols

length = int(input('Enter password length: '))
password = ''.join(random.choice(all_chars) for _ in range(length))

print('Generated Password:', password)
