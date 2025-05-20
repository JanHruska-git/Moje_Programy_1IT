count = 0
for a in (2, 4, 6, 8):
    for b in range(1, 10):
        for c in range(1,10):
            for d in range(1,5):
                if a + b + c + d == 21:
                    print(a,b,c,d)
                    count += 1
print(f"Pocet cifer: {count}")