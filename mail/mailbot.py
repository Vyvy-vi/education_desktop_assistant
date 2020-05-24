import smtplib, ssl
def mail():
    print('....1- Send 1 mail to 1 recipient\n\
....2- Send 1 mail to multiple recipients.\n\
....3- Ping the mailbot.')
    opt=int(input('Enter the Action you would like to perform:'))
    if opt==1:
        m1()
    elif opt==2:
        mm()
    elif opt==3:
        ping()
    else:
        print('ERROR!- Value entered isn\'t corresponding to menu options.')
mail()
#TODO- Add option to use own mail rather than the mail of the bot account.
def m1(subject,recp,sender,data):
    msg=f"\
            Subject:{(input(subject}\n\n{data}\nFrom:{sender}"
    context= ssl.create_default_context()
    s= smtplib.SMTP('smtp@gmail.com', 587)
    s.starttls(contxt = context)
    s.login("archimedesmailbot@gmail.com", "@rchimedes")
    try:
        s.sendmail("archimedesmailbot@gmail.com",recp,msg)
        s.quit()
        return 'success'
    except Exception as e:
        s.quit()
        return e






"""
msg=f"\
        Subject:{(input('Enter subject:'))}\n\nDid you get spam mailed?"
context = ssl.create_default_context()
id= input('Enter id to which you want to send email:')
for i in range(1,int(input('This program sends emails in batches of 10.\nEnter no. of batches:'))+1):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls(context= context)
    s.login("archimedesmailbot@gmail.com", "@rchimedes")
    for j in range(1,11):
        try: 
            s.sendmail("archimedesmailbot@gmail.com", id, msg)
            print(f'success #{i}.{j}')
        except:
            print(f'failed #{i}.{j}') 
    s.quit()
"""
