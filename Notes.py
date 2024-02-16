import collections
import os.path
from colorama import Fore
from collections import namedtuple
from datetime import date

import Executor


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
        data[str(newIndex)] = newNote

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

    footerCommand("\n('p номер_заметки' - открыть заметку\n"
                  "'red номер_заметки' - редактировать заметку\n"
                  "'del номер_заметки' - удалить заметку\n"
                  "'m' - назад): ", data)


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
        print(str(key) + " - " + str(value) + " (" + str(dateInfoDict[value]) + niceRussianNotes(
            str(dateInfoDict[value])) + ")")

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


def footerCommand(text, data, id=None):
    wait = True
    # while wait:
    charin = input(text)
    wait = Executor.doCommand(charin, data, id)
    # return False


def printNote(data, id):
    if data.get(id) == None:
        print("Заметки с таким номером не существует")
        footerCommand("Повторите ввод: ", data)
        return
    printChangeText = ""
    horLine = "="*25
    if data[id][2] != data[id][3]:
        printChangeText = ", изменена " + data[id][3]

    print("")
    print(Fore.YELLOW ,horLine + "Заметка номер: " + id + " от " + data[id][2] + printChangeText+horLine)
    print("Заголовок: " + data[id][0])
    print("Текст: \n" + data[id][1])
    print(Fore.RESET)

    footerCommand("('del' - удалить заметку\n"
                  "'red' - редактировать заметку\n"
                  "'m' - возврат в главное меню): ", data, id)


def deleteNote(data, id):
    if data.get(id) == None:
        print("Заметки с таким номером нет")
        return
    data.pop(id)
    input("Заметка удалена, для продолжения нажмите любую клавишу...")


def changeNoteText(data, id):
    if data.get(id) == None:
        print("Заметки с таким номером нет")
        return
    print("Если не хотите менять заголовок или текст просто нажмите ENTER")
    print("Текущий заголовок:")
    print(Fore.YELLOW, data[id][0])
    print(Fore.RESET,"")
    newHeader = input("Новый заголовок: \n")
    isChanged = False
    if len(newHeader) != 0:
        data[id][0] = newHeader
        isChanged = True
    print("Текущий текст:")
    print(Fore.YELLOW, data[id][1])
    print(Fore.RESET, "")
    newText = input("Введите новый текст:\n")
    if len(newText) != 0:
        data[id][1] = newText
        isChanged = True

    if isChanged:
        changeDate = date.today().strftime("%d.%m.%Y")
        data[id][3] = changeDate
        input("Заметка удачно изменена, для продолжения нажмите любую клавишу...")
    else:
        input("Изменения не зафиксированы, нажмите любую клавишу...")