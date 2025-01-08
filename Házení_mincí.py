import random

print("Házení mincí!")

while True:
    vstup = input("Chcete házet mincí? (hazej): ")
    if vstup.lower() == "hazej":
       vysledek = random.choice(["Panna", "Orel"])
       print("Výsledek: ", vysledek)
   