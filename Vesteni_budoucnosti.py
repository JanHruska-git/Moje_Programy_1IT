import random
moznosti = ("ano", "ne","pravdepodobne ano","pravdepodobne ne")
otazka = input("zadej otazku.")
budoucnost = random.choice(moznosti)
print(budoucnost)
