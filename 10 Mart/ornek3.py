import random

x=random.randint(-10,10)

print("Rastgele seçilen artış sayınız:", x)

sayi1=int(input("Sayı 1:"))
sayi2=int(input("Sayı 2:"))

if x>0:
    for i in range(sayi1, sayi2, x):
        print(i)
        
if x<0:
    for i in range(sayi1, 0, x):
        print(i)
