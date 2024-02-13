import os

import Notes
import NotesRepository

print("Система работы с заметками. Укажите команду или 'q' для выхода")

data = NotesRepository.openRepository()

while(True):
    print("1. введите '+' для добавления заметки")
    charin = input()

    if charin == '+':
        Notes.addNote(data)
    elif charin == 'q':
        break

NotesRepository.saveRepository(data)