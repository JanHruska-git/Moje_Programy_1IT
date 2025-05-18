text = input("Zadej text: ")
pocet = int(input("Kolikrát ho chceš zopakovat? "))
for i in range(pocet):
    print(f"{i + 1}. {text}")