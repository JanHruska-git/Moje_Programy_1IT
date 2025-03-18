import random
čislo = random.randint(1, 10)
pokus = 0
počet_pokusu = 0
while pokus != čislo:
    pokus = int(input("hádej čislo od 1 do 10:"))
    počet_pokusu += 1
    
    if pokus < čislo:
       print("zkus víš")
    elif pokus > čislo:
       print("zkus níž")


print("Správně")
print("počet_pokusu: ", počet_pokusu)







