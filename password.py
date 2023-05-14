import random
from itertools import combinations
from string import ascii_uppercase, ascii_lowercase, digits, punctuation

special_symbols = punctuation.replace('<', '').replace('>', '')

special_case = "".join((
    random.choice(ascii_lowercase),
    random.choice(ascii_uppercase),
    random.choice(digits),
    random.choice(special_symbols)))
password_length = 8
all_symbols = ascii_uppercase + ascii_lowercase + digits + special_symbols
differance = random.choice(tuple(combinations(all_symbols, password_length - len(special_case))))
full_password=list(special_case+"".join(differance))
random.shuffle(full_password)
print("".join(full_password))
