n = int(input("Введите число n: "))
if n<=100:
    for i in range(1,n+1): 
        print(sum([x for x in range(i+1)]), end=' ')
elif n>100:
    for i in range(1,101): 
        print(sum([x for x in range(i+1)]), end=' ')
