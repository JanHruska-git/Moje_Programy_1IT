vaha = float(input("Zadej svoji vahu(kg): "))
vyska_cm = float(input("Zadej svoji vysku (cm): "))
bmi = vaha / ((vyska_cm / 100) ** 2)
if bmi <= 18.5:
	print(bmi, "Mas podvahu")
elif 18.5 <= bmi < 24.9:
	print(bmi, "Mas normlani vahu")
elif 25 <= bmi < 29.9:
	print(bmi, "Mas nadvahu")
elif bmi >= 30:
	print(bmi, "Mas obezitu")
	
	
