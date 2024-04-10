import csv


def find_note_id(title): 
    with open("notes.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == title:
                return row,
    print("Заголовок не найден")
    return -1