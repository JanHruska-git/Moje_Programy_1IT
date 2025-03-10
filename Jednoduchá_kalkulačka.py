čislo= float(input("Napiš první číslo: "))
print("vyber operaci: 1 = +, 2 = -, 3 = *, 4 = /")
funkce = int(input("napiš operaci: "))
čislo2 = float(input("Napiš druhé číslo: "))
if funkce == 1:
    vysledek = čislo + čislo2
elif funkce == 2:
    vysledek = čislo - čislo2
elif funkce == 3:
    vysledek = čislo * čislo2
elif funkce == 4:
    vysledek = čislo / čislo2

print ("výsledek: ", vysledek)



