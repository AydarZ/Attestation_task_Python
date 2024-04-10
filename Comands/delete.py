import csv
from Comands.find_note_id import find_note_id


def del_note():
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
        with open("notes.csv", "w", newline='') as file:
                writer = csv.writer(file)                        
                writer.writerows(lines)