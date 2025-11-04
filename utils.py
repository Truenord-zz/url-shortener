import random
import string
# utility functions, one file for now.
# probabily we should generate the new urls here

def short_url_generator(new_url_length = 6):
    chars = string.digits + string.ascii_letters
    new_url = ''.join(random.choice(chars) for i in range(new_url_length))
    return new_url

print(short_url_generator())