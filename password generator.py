import random
import string

length = int(input("Enter desired password length: "))
chars = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(chars) for _ in range(length))
print("Generated Password:", password)
