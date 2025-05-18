text = input("Zadej text: ")
samohlasky = "aeiouáéíóúůAEIOUÁÉÍÓÚŮ"
pocet = sum(1 for znak in text if znak in samohlasky)
print("Počet samohlásek:", pocet)
