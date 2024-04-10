import csv

from Comands.add import add_note
from Comands.delete import del_note
from Comands.edit import edit_note
from Comands.print import print_note
from Comands.print_all import print_all_note
from Comands.print_date import print_date





def input_comand(id_notes):
    while True:
        command = input("Введите команду(add, del, edit, print, print_all, print_date): ")
        if(command == "add"):
            add_note(id_notes)
        elif (command == "del"):
            del_note()
        elif (command == "edit"):
            edit_note()
        elif (command == "print"):
            print_note()
        elif (command == "print_all"):
            print_all_note()
        elif (command == "print_date"):
            print_date()    
        else: print("Введена неверная команда")

with open("notes.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(
        ("id","Title","Body","Date")
    )

id_notes = set()
input_comand(id_notes)