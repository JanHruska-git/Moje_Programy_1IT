score = 0
print("Kviz o me")
print("1. Kdy jsem se narodil?")
odpoved = input("1. 5.9.2009  2. 10.1.2009  3. 20.3.2008:  ")
if odpoved == "2":
	print("Spravne!")
	score += 1
print("2. co mam za mazlicka?")
odpoved = input("1. Kocka  2. jednorozec  3. pes:  ")
if odpoved == "3":
	print("Spravne!")
	score += 1
print("3. Jakej obor se ucim?")
odpoved = input("1. IT  2. ITE  3. Skibidi toilet obor:  ")
if odpoved == "1":
	print("Spravne!")
	score += 1
print(f"Konec kvizu tvoje skore je {score}/3")

