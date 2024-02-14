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
            textNote = textNote + s + "\n"
            s = ""

    currentDate = currentDate.strftime("%d.%m.%Y")
    note = namedtuple('note', ['head', 'text', 'dateCreate', 'dateChange'])

    newNote = note(headNote, textNote, currentDate, currentDate)

    if len(data) == 0:
        data[0] = newNote
    else:
        sorted(data.keys())
        lastIndex = int(next(reversed(data)))
        newIndex = lastIndex + 1
        data[newIndex] = newNote

    print("Заметка сохранена")


def printAllNotes(data):
    maxLengthHead = 45
    maxLenghtText = 71
    maxLenghtId = 7
    sp = ' '
    idHeadText = " НОМЕР "

    for key, value in data.items():
        tempKey = toString(key)

        if maxLenghtId < len(tempKey):
            maxLenghtId = len(tempKey)

    if len(idHeadText) < maxLenghtId:
        idHeadText = getFormalizeText(idHeadText, maxLenghtId, "   ")

    print(
        "|" + idHeadText + "|" + sp * 18 + "ЗАГОЛОВОК" + sp * 18 + "|" + sp * 33 + "ТЕКСТ" + sp * 33 + "|" + " ДАТА СОЗДАНИЯ |" + " ДАТА ИЗМЕНЕНИЯ |")
    lenHorizontalLine = maxLenghtId + maxLengthHead + maxLenghtText + 6 + 15 + 16
    print('_' * lenHorizontalLine)

    for key, value in data.items():
        tempKey = toString(key)
        idText = "|" + sp * (7 - len(tempKey)) + tempKey

        headText = getFormalizeText(value[0], maxLengthHead, "...")
        noteText = getFormalizeText(value[1], maxLenghtText, "...")
        createDateText = getFormalizeText(value[2], 15, "...")
        changeDateText = getFormalizeText(value[3], 16, "...")

        print(idText + headText + noteText + createDateText + changeDateText + "|")
        print('_' * lenHorizontalLine)

    input("\nнажмите любую клавишу...")
def getAllNotesDateCreate(data):
    tempData = collections.OrderedDict()

    dateDict = collections.OrderedDict()
    dateInfoDict = collections.OrderedDict()

    for key, value in data.items():
        dateString = toString(value[2])
        if dateInfoDict.get(dateString) == None:
            dateInfoDict[dateString] = 1
        else:
            dateInfoDict[dateString] += 1

    index = 1
    for key, value in dateInfoDict.items():
        dateDict[index] = key
        index += 1

    print("Выберите дату, 'q' - выход")

    for key, value in dateDict.items():
        print(str(key) + " - " + str(value) + " (" + str(dateInfoDict[value]) + niceRussianNotes(str(dateInfoDict[value])) +")")

    notValidIndex = True
    dateIndex = 0
    currenDate = ""
    while notValidIndex:
        dateIndex = input()
        if dateIndex == 'q':
            return
        if dateDict.get(int(dateIndex)) != None:
            currenDate = dateDict.get(int(dateIndex))
            notValidIndex = False
        print("Укажите дату из списка")

    for key, value in data.items():
        if value[2] == currenDate:
            tempData[key] = value

    printAllNotes(tempData)


def toString(key):
    tempKey = key
    if isinstance(tempKey, int):
        tempKey = str(tempKey)
    return tempKey


def niceRussianNotes(string):
    ls = string[-1]
    if ls == "1":
        return " заметка"
    if ls == "2" or ls == "3" or ls == "4":
        return " заметки"
    return " заметок"


def getFormalizeText(text, lenght, addFinalText):
    text = text.replace('\n', ' ')
    if len(text) > lenght:
        head = text[:lenght - 3] + addFinalText
    else:
        left = int((lenght - len(text)) / 2)
        head = ' ' * left + text
    headText = "|" + head + ' ' * (lenght - len(head))
    return headText
