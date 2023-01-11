#ülesanne 0. Leida arvude jada summa vahemikus 1 kuni 100. Kuvade tulemus ekraanil. Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
#For tsükkel цикл For
s = 0
for i in range(0,101): #выводит диапазон чисел от нуля до 101 и наждое следующее число прибавляется на порядковое предыдущего. 
    s+=i 
    print(s) 
i = 0 
#while tsükkel цикл while
s = 0
while i<= 100: 
    s+=1 
    i+=1 
    print(s)
#ülesanne 2. Koosta programm, mis küsib kasutajalt 10 korda arve ja väljastab seejärel nende arvude summa.
#Täienda seda programmi nii, et kasutajalt küsitakse arve seni, kuni kasutaja enam uut arvu ei sisesta, vaid vajutab lihtsalt sisestusklahvi.
#Proovige seda ülesannet lahendada nii while- kui for-tsükliga. Написать программу, которая 10 раз запрашивает число у пользователя, а затем выводит сумму этих чисел. Улучщить эту программу так, чтобы у пользователя до сил пор спрашивалось число и он не выводил новый номер, а просто нажимал.


#10 
x = 1
while True:
    if x>100: 
        break
    elif x%5==0:
        print(x,end=" ")
    x+=1

for x in range(1,100,1):
    if x%5==0:
        print(x,end=" ")

from math import*
from random import*
try:
    num_horiz=int(input("sisesta ruutude arv horisontaalselt =>> \n"))
except:
    print("value Error")
    num_horiz=randint(1,10000)
try:
    num_vert=int(input("sisesta ruutude arv vertikaalselt =>> \n "))
except:
    print("Value Error")
    num_vert=randint(1,20)

for y in range(num_vert):
    for x in range(num_horiz):
        print("o", end=" ")
    print()




