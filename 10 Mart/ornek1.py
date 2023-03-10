import random

x = int(input("1-10 arası sayı giriniz."))

if x>10 or x<1:
    print("Tekrar dene!")
    x = int(input("1-10 arası sayı giriniz."))

y = random.randint(11,50)
print("Rastgele seçilen bitiş sayınız:", y)

t=0

for i in range(x,y):
    if i%3==0:
        print(i)
        t=t+i

print("Toplam:", t)
