import datetime
import json

from Note import Note

import json

class NoteManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.notes = []
    
    def load_notes(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                self.notes = [
                    Note(note['note_id'], note['title'], note['body'], datetime.datetime.fromisoformat(note['timestamp']))
                    for note in data
                ]
            print("Заметки успешно загружены.")
        except FileNotFoundError:
            print("Файл с заметками не найден.")
    
    def save_notes(self):
        data = [
            {'note_id': note.note_id, 'title': note.title, 'body': note.body, 'timestamp': note.timestamp.isoformat()}
            for note in self.notes
        ]
        with open(self.file_path, 'w') as file:
            json.dump(data, file)
    
    def add_note(self, title, body):
        note_id = len(self.notes) + 1
        note = Note(note_id, title, body)
        self.notes.append(note)
        self.save_notes()
        print("Заметка успешно добавлена.")
    
    def edit_note(self, note_id, title, body):
        note = self.get_note_by_id(note_id)
        if note:
            note.title = title
            note.body = body
            note.timestamp = datetime.datetime.now()
            self.save_notes()
            print("Заметка успешно отредактирована.")
        else:
            print("Заметка с указанным ID не найдена.")
    
    def delete_note(self, note_id):
        note = self.get_note_by_id(note_id)
        if note:
            self.notes.remove(note)
            self.save_notes()
            print("Заметка успешно удалена.")
        else:
            print("Заметка с указанным ID не найдена.")
    
    def read_notes_by_date(self, date):
        filtered_notes = [note for note in self.notes if note.timestamp.date() == date]
        
        if filtered_notes:
            for note in filtered_notes:
                print(f"[ID: {note.note_id}] {note.title} ({note.timestamp}) - {note.body}")
        else:
            print("Заметки на указанную дату не найдены.")
    
    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                return note
        return None
    
    def get_all_notes(self):
        for note in self.notes:
            print(f"[ID: {note.note_id}] {note.title} ({note.timestamp}) - {note.body}")