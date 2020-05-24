import os
import datetime
from fileexistcheck import fileexists
#TODO- Add date-time to File?
#TODO- Fxn. to do specific alterations.(by launching a prompt/ gui/...)
def makenote(filename, text):
    check= fileexists()
    if check==False:
        with open(filename,'w') as f:
            f.write(text)
        return 'Note Added.'
    else:
        return overnote(filename, text)

def overnote(filename, text):
    with open(filname,'w') as f:
        f.write(text)
    return 'A previous instance of this note was found. It has been Overwritten.'
    
def editnote(filename, text):
    check= fileexists()
    if check==False:
        return 'This note does not exist.'
    else:
        with open(filename, 'a') as f:
            f.write(text)
        return  'The note has been Edited.'

def readnote(filename):
    check= fileexists()
    if check==False:
        return 'This note does not exist.'
    else:
        with open(filename) as f:
            fl= f.read()
            return fl

def alternote(filename):
    #TODO



