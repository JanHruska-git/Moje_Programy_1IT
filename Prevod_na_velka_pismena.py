text = input("Zadej text: ")
mala = sum(1 for znak in text if znak.islower())
velka = sum(1 for znak in text if znak.isupper())
print("Malá písmena:", mala)
print("Velká písmena:", velka)