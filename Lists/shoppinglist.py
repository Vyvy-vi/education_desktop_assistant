def makelist(name, items: list):
    name= './'+name+'.txt'
    with open(name,"w") as f:
        for i in range(len(items)):
            f.write(f'{i+1}- {items[i]}\n')
        return 'List has been Made.'
def dellist(name):
    name= './'+name+'.txt'
    #TODO
def readlist(name):
    name= './'+name+'.txt'
    with open(name) as f:
        return f.read()
def addtolist(name,items: list):
    name= './'+name+'.txt'
    with open(name) as f:
        r= len(f.readlines())
    with open(name,'a+') as f:
        for i in items:
            f.write(f'{r+i+1}- {items[i]}\n')
        p=f'{len(items)} items added to the list...'
        return p
def remlist(name, entry):
    name= './'+name+'.txt'
    with open(name, 'r+') as f:
        p= f.readlines()
        for i in range(len(p)):
            if p[i]== entry:
                p.pop(i)
        f.write(p)
        pr=f'Entry has been Removed.'
        return pr
