import os

import Notes
import NotesRepository

data = NotesRepository.openRepository()

while(True):
    os.system('cls')
    print("====================================Заметки====================================")
    print("1. введите '+' для добавления заметки\n"
          "2. введите 'all' для получения списка заметок\n"
          "(без параметров - как есть, '-d' - за выбранную дату)\n"
          "3. введите 'q' для выхода из программы")
    charin = input()

    if charin == '+':
        Notes.addNote(data)
    elif charin == 'all':
        Notes.printAllNotes(data)
    elif charin == 'all -d':
        Notes.getAllNotesDateCreate(data)
    elif charin == 'q':
        break

NotesRepository.saveRepository(data)