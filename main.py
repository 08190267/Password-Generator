import random
import string

print('=== Password Generator ===')
length = int(input('Enter password length: '))
use_symbols = input('Include symbols? (y/n): ').lower()

chars = string.ascii_letters + string.digits
if use_symbols == 'y':
    chars += string.punctuation

password = ''.join(random.choice(chars) for _ in range(length))

print('\nGenerated Password:', password)
