import random

user_entry = str(input('\n Entre o texto: '))
aleatory_chars = '!12@#3$4%5¨6&7*8(9)0_-+=§Qwertyuiopasdfghjklçzxcvbnm></?'
crypto = 'init'

for char in user_entry.upper():
    for c in range(0, 3):
        crypto += random.choice(aleatory_chars)


print(crypto) 
