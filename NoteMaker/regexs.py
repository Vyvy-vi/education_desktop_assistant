from colorama import Fore, Style, Back
import os
from fileexistcheck import fileexists
def regex(path, find, rep=None):
    if fileexists() == False:
        return 'File not found in given path'
    fl = open(path,"r+")
    fl.seek(0,os.SEEK_SET)
    l=fl.read()
    k = find
    r= k if rep==None else rep
    return highlight(k,l,r)

def highlight(k,l,r):
    if l.startswith(k) == False and l.endswith(k) == False:
        p= l.split(k)
        s=f'{Back.BLUE}{r}{Style.RESET_ALL}'
        return s.join(p)
    elif(l.startswith(k)==False):
        p= l[0:-1].split(k)
        s=f'{Back.BLUE}{r}{Style.RESET_ALL}'
        return s.join(p)+s    
    
    
    elif(l.endswith(k)==False):
        p= l[1:].split(k)
        s=f'{Back.BLUE}{r}{Style.RESET_ALL}'
        return s+s.join(p)
    
    else:
        p= l[1:-1].split(k)
        s=f'{Back.BLUE}{r}{Style.RESET_ALL}'
        return s+s.join(p)+s       


