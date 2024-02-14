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
    note = namedtuple('note',['head', 'text', 'dateCreate', 'dateChange'])

    newNote = note(headNote, textNote, currentDate, currentDate)

    # data = collections.OrderedDict()

    if len(data) == 0:
        data[0] = newNote
    else:
        sorted(data.keys())
        lastIndex = int(next(reversed(data)))
        newIndex = lastIndex + 1
        data[newIndex] = newNote

    print("Заметка сохранена")

def getAllNotes(data):
    maxLengthHead = 45
    maxLenghtText = 71
    maxLenghtId = 7
    sp = ' '
    idHeadText = " НОМЕР "

    for key,value in data.items():
        tempKey = toString(key)

        if maxLenghtId < len(tempKey):
            maxLenghtId = len(tempKey)

    if len(idHeadText) < maxLenghtId:
        idHeadText = getFormalizeText(idHeadText, maxLenghtId, "   ")

    print("|"+idHeadText+"|" + sp*18 + "ЗАГОЛОВОК" + sp*18+"|" + sp*33 + "ТЕКСТ" + sp*33 + "|" + " ДАТА СОЗДАНИЯ |" + " ДАТА ИЗМЕНЕНИЯ |")
    lenHorizontalLine = maxLenghtId+maxLengthHead+maxLenghtText+6+15+16
    print('_'*lenHorizontalLine)

    for key, value in data.items():
        tempKey = toString(key)
        idText = "|"+sp*(7-len(tempKey))+tempKey

        headText = getFormalizeText(value[0], maxLengthHead, "...")
        noteText = getFormalizeText(value[1], maxLenghtText,"...")
        createDateText = getFormalizeText(value[2], 15,"...")
        changeDateText = getFormalizeText(value[3], 16,"...")

        print(idText + headText + noteText + createDateText + changeDateText + "|")
        print('_' * lenHorizontalLine)

def toString(key):
    tempKey = key
    if isinstance(tempKey, int):
        tempKey = str(tempKey)
    return tempKey

def getFormalizeText(text, lenght, addFinalText):
    text = text.replace('\n', ' ')
    if len(text) > lenght:
        head = text[:lenght-3] + addFinalText
    else:
        left = int((lenght - len(text)) / 2)
        head = ' ' * left + text
    headText = "|" + head + ' ' * (lenght - len(head))
    return headText