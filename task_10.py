n = int(input("Введите кол-во монет: "))
count_orel=0
count_reshka=0
while n <= 0 or n == 1 :
    n = int(input("Некорректное число монет, введите кол-во монет: "))
for i in range(n) :
    a = int(input("Введите 1 для орла и 0 для решки: "))
    if a == 0:
        count_reshka +=1
        i +=1
    elif a == 1:
        count_orel +=1
        i +=1
    else:
        print("Вы ввели некорректное число, потворите ввод")
if count_orel > count_reshka:
    print(f'Небходимо перевернуть {count_reshka} решек, так как их меньше')
elif count_reshka > count_orel:
    print(f'Небходимо перевернуть {count_orel} орлов, так как их меньше')
elif count_orel == 0 or count_reshka == 0:
    print("Нет необходимости, что либо переворачивать, так как вы ввели, что на столе вск монеты одной стороны")
else :
    print("На столе лежит одинаковое количество монет с решками и орлами")