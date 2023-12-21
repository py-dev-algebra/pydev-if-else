# Generated 2 paragraphs, 160 words

# ZADATAK: U generičkom tekstu 'Lorem ipsum ...' (https://www.lipsum.com/)
# pronađite koliko puta se pojavljuje neka riječ, recimo sit

text = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
        'Duis convallis lorem efficitur lorem luctus, et aliquam orci accumsan. '
        'Integer ligula eros, aliquet interdum massa sed, aliquam suscipit lectus. '
        'Nunc dapibus, nisl vel finibus tempor, turpis purus suscipit ipsum, sed euismod justo magna ac lorem. '
        'Pellentesque placerat mauris quis nulla interdum, at suscipit ipsum vulputate. '
        'Proin efficitur nunc dui, vulputate faucibus quam rutrum sed. '
        'Pellentesque orci diam, vehicula sit amet nulla vitae, iaculis consectetur nulla. '
        'Phasellus eleifend purus lorem, et gravida nunc aliquam et. '
        'Morbi neque mauris, vestibulum at lorem luctus, condimentum viverra mauris. '
        ' '
        'Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; '
        'Vivamus nec placerat lectus, sed pharetra sem. '
        'Proin feugiat dapibus ante et varius. Sed quis dolor purus. '
        'Maecenas porttitor est non risus dapibus volutpat. '
        'Pellentesque dapibus luctus sapien in feugiat. '
        'Nulla eu consectetur ipsum. '
        'Sed in vulputate diam. '
        'Nunc lacinia, dolor nec facilisis suscipit, lacus nibh rhoncus ex, vitae venenatis enim orci eget nunc.')

print(text)

# riječi_teksta = text.split()
# print(riječi_teksta)
# broj = riječi_teksta.count('nulla')
# print(broj)

rijeci = text.split(' ')
# rijeci = rijeci.lower()

# rijeci_lower = []
# rijeci_lower = [rijec.lower() for rijec in rijeci]

for rijec in rijeci:
    #original_rijec = rijec
    index_rijec = rijeci.index(rijec)

    # if rijec ima znak '.':
    if '.' in rijec:
        rijec = rijec.replace('.', '')
    elif ';' in rijec:
        rijec = rijec.replace(';', '')
    elif ',' in rijec:
        rijec = rijec.replace(',', '')
    elif '!' in rijec:
        rijec = rijec.replace('!', '')


    #rijeci[rijeci.index(original_rijec)] = rijec.lower()
    rijeci[index_rijec] = rijec.lower()




rijec = input('Unesite rijec: ')
word_count = rijeci.count(rijec) 
print(word_count)
