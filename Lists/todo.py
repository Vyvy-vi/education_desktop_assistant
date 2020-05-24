def makelist(items: list,date):
    name= './'+date+'.txt'
    with open(name,"w") as f:
        for i in range(len(items)):
            f.write(f'{i+1}- {items[i]}\n')
        return 'ToDo List has been created.'
def dellist(date):
    name= './'+date+'.txt'
    #TODO
def readlist(date):
    name= './'+date+'.txt'
    with open(name) as f:
        return f.read()
def addtolist(date,items: list):
    name= './'+date+'.txt'
    with open(name) as f:
        r= len(f.readlines())
    with open(name,'a+') as f:
        for i in items:
            f.write(f'{r+i+1}- {items[i]}\n')
        p=f'{len(items) ToDos Added}...'
        return p
def remlist(date, entry):
    name= './'+date+'.txt'
    with open(name, 'r+') as f:
        p= f.readlines()
        for i in range(len(p)):
            if p[i]== entry:
                p.pop(i)
        f.write(p)
        pr=f'ToDo has been Removed.'
        return pr
