import random

bas=random.randint(1, 20)
son=random.randint(30, 100)

t=0

for i in range(bas, son):
    if i%5==0:
        print(i)
        t=t+i

print("Toplam:", t)
