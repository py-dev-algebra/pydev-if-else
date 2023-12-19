# ZADATAK: Napišite program koji provjerava je li unesena riječ palindrom.
    # Palindrom je riječ koja se jednako piše (i čita) s lieva na desno i s desna na lijevo

rijec = input('Upisite rijec: ') # Kapak
# rijec = rijec.lower() # kapak
obrnuta_rijec = rijec[ : : -1] # kapak

if rijec.lower() == obrnuta_rijec.lower():
    print(f'Rijec {rijec} JE palindrom!')
else:
    print(f'Rijec {rijec} NIJE palindrom!')




# lista1 = list(rijec)
# print(lista1)

# # lista2 = lista1.pop()
# # print(lista1)

# lista2 = lista1[ : : -1]
# print(lista2)


# if lista1 == lista1.reverse():
#     print("palindrom")

# if lista1 == lista2:
#     print("palindrom")