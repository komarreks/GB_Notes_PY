import os

import Notes
import NotesRepository

data = NotesRepository.openRepository()

while(True):
    print("1. введите '+' для добавления заметки\n"
          "2. введите 'all' для получения списка заметок")
    charin = input()

    if charin == '+':
        Notes.addNote(data)
    elif charin == 'all':
        Notes.getAllNotes(data)
    elif charin == 'q':
        break

NotesRepository.saveRepository(data)