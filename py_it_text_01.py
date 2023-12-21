recenica = 'Python je super jednostavan programski jezik'
print(f'Original: {recenica}')

# Pretvara sva slova teksta u mala slova - lowercase
recenica = recenica.lower()
print(f'Lower: {recenica}')

# Pretvara sva slova teksta u velika slova - uppercase
recenica = recenica.upper()
print(f'Upper: {recenica}')

# Pretvara prvo slovo teksta u veliko pocetno slovo
recenica = recenica.capitalize()
print(f'Capitalize: {recenica}')

# Pretvara prvo slovo teksta svake rijeci u veliko pocetno slovo
recenica = recenica.title()
print(f'Title: {recenica}')

print('\n')


recenica = 'Python je super jednostavan programski jezik.'
rijeci_recenice = recenica.split(sep=' ')
print(f'Split: {rijeci_recenice}')


print('\n')
rijec = 'Python!'
print(f'Original: {rijec}')

rijec = rijec.replace('!', '')
print(f'Replace1: {rijec}')

rijec = rijec.replace('th', 'TH')
print(f'Replace2: {rijec}')
