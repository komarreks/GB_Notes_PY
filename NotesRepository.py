import collections
import json
import os.path
from collections import namedtuple


def openRepository():
    createRepository()
    with open("notes/notes.json",'r+') as jsonfile:
        return json.load(jsonfile)

def createRepository():
    checkWorkDirectory()
    if not os.path.exists("notes/notes.json"):
        # note = namedtuple('note',['head', 'text', 'dateChange'])
        data = collections.OrderedDict()
        # data.setdefault(int, note)
        # newNote = note('Заголовок','текст','дата')
        # data[0] = newNote
        with open("notes/notes.json",'w') as jsonFile:
            json.dump(data, jsonFile)

def checkWorkDirectory():
    if not os.path.isdir("notes"):
        os.mkdir("notes")

def saveRepository(data):
    with open("notes/notes.json", 'w') as jsonFile:
        json.dump(data, jsonFile)