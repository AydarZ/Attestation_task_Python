import csv
import datetime
import random


def add_note(id_notes):
    list = []
    id = 0
    while(id == 0):
        id_temp = random.randint(0,999999999999)
        if id_temp in id_notes:
            continue
        id_notes.add(id_temp)
        id = id_temp
    list.append(id)    
    list.append(input("Введите заголовок заметки: "))
    list.append(input("Введите тело заметки: "))
    list.append(datetime.datetime.now())
    with open("notes.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(list)
    print("Заметка успешно сохранена")