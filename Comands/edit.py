import csv
import datetime
from Comands.find_note_id import find_note_id


def edit_note():
    title = input("Введите заголовок заметки: ")
    id = find_note_id(title)
    if (id == -1):
        return
    else:
        del_index =-1
        with open("notes.csv", "r") as file:
            reader = csv.reader(file)
            lines = list(reader)
            for i in range(len(lines)):
                if (lines[i][0] == id[0][0]):
                    del_index = i
                    break
            lines.pop(del_index)
            list_ = []
            list_.append(id[0][0])    
            list_.append(input("Введите новый заголовок заметки: "))
            list_.append(input("Введите новое тело заметки: "))
            list_.append(datetime.datetime.now())
            lines.insert(del_index, list_)        
        with open("notes.csv", "w", newline='') as file:
                writer = csv.writer(file)                        
                writer.writerows(lines)