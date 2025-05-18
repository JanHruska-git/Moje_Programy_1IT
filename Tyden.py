den = input("Zadej den v týdnu: ").lower()
if den in ["sobota", "neděle"]:
    print("Je víkend!")
else:
    print("Je pracovní den.")