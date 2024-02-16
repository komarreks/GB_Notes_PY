import Notes


def doCommand(charin, data, id=None):
    if charin == '+':
        Notes.addNote(data)
    elif charin == 'all':
        Notes.printAllNotes(data)
    elif charin == 'all -d':
        Notes.getAllNotesDateCreate(data)
    elif charin[:1] == 'p':
        Notes.printNote(data, charin[2:])
    elif charin[:3] == 'del':
        if id != None:
            Notes.deleteNote(data, id)
        else:
            Notes.deleteNote(data, charin[4:])
    elif charin[:3] == 'red':
        if id != None:
            Notes.changeNoteText(data, id)
        else:
            Notes.changeNoteText(data, charin[4:])
    elif charin == 'm':
        return False
    else:
        charin = input("Команда не распознана, повторите ввод: \n")
        doCommand(charin, data, id)
    return True