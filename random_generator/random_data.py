import random
import string

def generate_random_email(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

print (generate_random_email(7)+"@gmail.com")
