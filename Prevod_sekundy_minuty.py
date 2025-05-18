sek = int(input("Zadej sekundy: "))
minuty = sek // 60
zbytek = sek % 60
print(f"{minuty}:{zbytek:02}")