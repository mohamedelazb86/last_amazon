import random

def generate_code(length=8):
    data='0123456789ABCDEFGHIJKLMNOPQWXYZSRTV'
    code=''.join(random.choice(data)for _ in range(length))
    return code