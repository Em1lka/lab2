import re
lenbuf = 1
workbuf = ""
buf = ""
k = 4
flag = False
try:

    with open("lab2.txt", "r") as file:
        print("\nРезультат работы программы: \n")
        buf = file.read(lenbuf)                                     #чтение буфера

        if not buf:              #если буфер пустой
            print("\n Рабочий файл пустой, измените содержание файла:")

        while buf:                      #если буфер не пустой
            workbuf += buf                  #заполнение рабочего буфера символами из файла
            if re.findall(r'[.!?]', buf):   #если найдет .?! знак
                flag = True
                str = re.split(r'\W', workbuf)  #сплитуем по словам
                str = str[:len(str)-1]          #удаляем пробел от знака препинания
                if len(str) == k:               #если длина строки равна заданному количеству слов
                    print(workbuf)
                workbuf = ""
                str = ""
            buf = file.read(lenbuf)

        if flag == False:          #если в файле отсутствуют знаки то ->
            print("\nВ файле *.txt нет знаков окончания предложения!\n")


except FileNotFoundError:
    print("\n Файл *.txt в директории проекта не обнаружен.")