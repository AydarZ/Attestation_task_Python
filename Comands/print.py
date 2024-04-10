from Comands.find_note_id import find_note_id


def print_note():
    title = input("Введите заголовок заметки: ")
    id = find_note_id(title)
    if (id == -1):
        return
    else:
        print (*id)