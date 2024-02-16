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
    elif charin == 'm':
        return False
    else:
        print("Команда не распознана, проверьте ввод")
    return True