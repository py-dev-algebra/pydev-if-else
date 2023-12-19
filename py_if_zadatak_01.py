# ZADATAK: Kreirajte listu od 1 do broja 30. Ispišite sve brojeve koji su djeljivi s 3, 6 i 9
    # Provjera je li broj djeljiv s nekim drugim radimo pomoću % (modulo) operanda.
    # 15 % 3 NEMA ostatka, odnosno to je 0 pa je 15 djeljiv s 3.
    # 16 % 3 je 1, odnosno NIJE jednak 0 pa 16 NIJE djeljiv s 3.

# brojevi = [range(1, 31)]
# brojevi = list(range(1, 31))
brojevi = []
for broj in range(1, 31):
    brojevi.append(broj)


# print(4 / 3) # 1.3333333
# print(4 // 3) # 1


for broj in brojevi:
    if broj % 9 == 0:
        print(f'Broj {broj} je djeljiv s 9')
    
    if broj % 6 == 0:
        print(f'Broj {broj} je djeljiv s 6')
    
    if broj % 3 == 0:
        print(f'Broj {broj} je djeljiv s 3')
    else:
        print(f'Broj {broj} NIJE djeljiv s 3, 6 ili 9')
    
# for broj in brojevi:
#     if broj % 3 == 0:
#         print(f'Broj {broj} je djeljiv sa 3')
#         if broj % 6 == 0:
#             print(f'Broj {broj} je djeljiv sa 6')
#             if broj % 9 == 0:
#                 print(f'Broj {broj} je djeljiv sa 3, 6 i 9')
