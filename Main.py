import os

import Executor
import Notes
import NotesRepository

data = NotesRepository.openRepository()

while(True):
    os.system('cls')
    print("====================================Заметки====================================")
    print("1. введите '+' для добавления заметки\n"
          "2. введите 'all' для получения списка заметок\n"
          "(без параметров - как есть, '-d' - за выбранную дату)\n"
          "3. Введите 'p номер_заметки' для вывода отдельной заметки\n"
          "4. введите 'q' для выхода из программы")
    charin = input()

    if charin == 'q':
        os.system('cls')
        break
    else:
        Executor.doCommand(charin, data)

NotesRepository.saveRepository(data)