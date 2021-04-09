from bs4 import BeautifulSoup
import codecs
import os
 
def main():
    #Функция открытия файла по руту
    def readFile(fileName):
        #Открывает HTML файл fileName 
        #Читая файл, как encode utf=8
        htmlCode = codecs.open(fileName, "r", "utf-8").read()
        return htmlCode 
    
    #Основная функция распарса 
    def nameParce(htmlDoc):
 
        #Задаем параметры супа
        htmlCode = BeautifulSoup(htmlDoc, 'html.parser')
        nameTag = htmlCode.body.find('p', attrs={'class': 'full_name'})
    
        #На тот случай если подобных тегов с классами больше. 
        for p in nameTag:
            if p: 
                p = p.split()
                #Проверяет длину ФИО, для правильного вывода  
                if (len(p) == 3): 
                    print(f"Ура! Мы нашли фамилию: {p[0]}, имя: {p[1]}, отчество: {p[2]}!")
                elif (len(p) == 2):
                    print(f"Ура! Мы нашли фамилию: {p[0]}, имя: {p[1]}!")
                elif (len(p) == 1):
                    print(f"Ура! Мы нашли фамилию: {p[0]}!")
                else:
                    print("Упс! Кажется, что-то слишком сложное :(")
        return 
 
    print('Прочитать html код с файла или текста?')
    print('0. Шатдаунт программы \n 1. Прочесть HTML с файла \n 2. Прочесть HTML с текста')
 
    while True:
        command = int(input())
 
        #Где switch cases когда они так нужны...
        if command == 0:
            print('Шатдаунт')
            break 
        elif command == 1:
            try:
                print('Задайте путь к файлу: ')
                fileRepo = input() #Тут можно седлать, чтобы код чекал, что вводные данные не int/float  
                nameParce(readFile(fileRepo))
                break
            except:
                print('Такого файла не существует или в нем неправильный HTML код')
        elif command == 2:
            try:
                print('Задайте HTML код') 
                html = str(input())
                nameParce(html)
                break
            except:
                print('Это точно HTML? Точно есть класс?')
        else:
            print('Комманда неизвестна. Попробуйте еще раз.')  
 
 
if __name__ == '__main__':
    main()
 
    
 
