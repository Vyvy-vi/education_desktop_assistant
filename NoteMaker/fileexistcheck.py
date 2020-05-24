def fileexists(filename):
   oldfile= True
    try:
        f= open(filename)
        f.read()
    except IOError:
        oldfile= False
    finally:
        close()
    return oldfile
