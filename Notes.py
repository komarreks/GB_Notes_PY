import collections
import os.path
from collections import namedtuple
from datetime import date

def addNote(data):
    currentDate = date.today()
    headNote = "";
    while headNote == "":
        headNote = input("укажите заголовок заметки: ")

    textNote = "";
    s = ""
    print("напишите текст заметки, а в конце ввод и введите 's' для сохранения\n")
    while s != "s":
        s = input()
        if s != "s":
            textNote = textNote+s+"\n"
            s = ""

    currentDate = currentDate.strftime("%d.%m.%Y")
    note = namedtuple('note',['head', 'text', 'dateChange'])

    newNote = note(headNote, textNote, currentDate)

    # data = collections.OrderedDict()

    if len(data) == 0:
        data[0] = newNote
    else:
        sorted(data.keys())
        lastIndex = int(next(reversed(data)))
        newIndex = lastIndex + 1
        data[newIndex] = newNote

    print("Заметка сохранена")

