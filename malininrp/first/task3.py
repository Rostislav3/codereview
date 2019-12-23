#Порахувати суму САМЕ чисел в списку

L=[1 ,22,35,76,'hi',[],22,'Bro']
sum=0
string=''
for i in range(len(L)):
    if (type(L[i])) == int:
        sum=sum +L[i]
    elif (type(L[i])) == str:
        string = string + L[i] + ''
    else:
        print("Не працює\n",L[i])
print("Сума чисел\n",sum)
print("Об'єднання рядків\n",string)