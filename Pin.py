import random
pin = "".join(str(random.randint(0, 9)) for _ in range(4))
print("Vygenerovaný PIN:", pin)