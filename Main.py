import datetime
from NoteManager import NoteManager


if __name__ == "__main__":
    file_path = "notes.json"
    note_manager = NoteManager(file_path)
    note_manager.load_notes()
    
    while True:
        print("\n=== Менеджер заметок ===")
        print("1. Просмотреть все заметки")
        print("2. Просмотреть заметку по ID")
        print("3. Добавить новую заметку")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Просмотреть заметки по дате")
        print("0. Выйти")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            note_manager.get_all_notes()
        elif choice == "2":
            note_id = int(input("Введите ID заметки: "))
            note = note_manager.get_note_by_id(note_id)
            if note:
                print(f"\n[ID: {note.note_id}] {note.title} ({note.timestamp}) - {note.body}")
            else:
                print("Заметка с указанным ID не найдена.")
        elif choice == "3":
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            note_manager.add_note(title, body)
        elif choice == "4":
            note_id = int(input("Введите ID заметки: "))
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            note_manager.edit_note(note_id, title, body)
        elif choice == "5":
            note_id = int(input("Введите ID заметки: "))
            note_manager.delete_note(note_id)
        elif choice == "6":
            date_str = input("Введите дату в формате ГГГГ-ММ-ДД: ")
            try:
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                note_manager.read_notes_by_date(date)
            except ValueError:
                print("Неверный формат даты.")
        elif choice == "0":
            break
        else:
            print("Неверный выбор.")