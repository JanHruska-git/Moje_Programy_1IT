import random

možnosti = ["kamen", "papir", "nuzky"]
pc = random.choice(možnosti)
hrac = input("Vyber kamen, papir nebo nuzky: ").lower()

print(f"Počítač vybral: {pc}")

if hrac == pc:
    print("Remíza")
elif hrac == "kamen" and pc == "nuzky" or hrac == "nuzky" and pc == "papir" or hrac == "papir" and pc == "kamen":
    print("Vyhral jsi")
else:
    print("Prohrál jsi")