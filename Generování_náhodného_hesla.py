import random
import string
heslo = ""
cislo = int(input("zadej jak dlouhy chces mit heslo: "))
for i in range(cislo):
	heslo += random.choice(string.ascii_letters)
print(heslo)