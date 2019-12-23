#Вивести усі слова котрі містять в слові велику букву

text=input("Введіть рядок\n")
words=text.split(" ")
for word in words:
    if(word[0].isupper()):
        print(word)