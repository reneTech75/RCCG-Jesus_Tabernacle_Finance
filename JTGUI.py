from PIL import ImageTk, Image
from tkinter import *
from tkinter import ttk
import datetime
import theSummary
#data=[]#this will be the list that holds member,amount,purpose, method and date

#this function collects data that will be sent to the data base.
def dataCollector(From='Submit or Save?'):
  data=[]
  global Amount,purposeBox,methodBox
  if From=='Submit and Close':
    print(From)
  
  if From=='Save':
    print(From)#debugger. Good
    data.append(memberBox.get())
    data.append(Amount.get())
    Amount.delete(0,END)
    data.append(methodBox.get())
    data.append(purposeBox.get())
    data.append(str(g.month)+'-'+str(g.day)+'-'+str(g.year))#i have it this way to put it in the US format
    
    #we are going to also save dada in a text document for redundancy
    file=open('dataLog.txt','at')
    file.write(str(data)+'\n')
    file.close()

    
    theSummary.summary(data[0])#call the summary() function and pass customer name
# this function closes the add member frame
def exitFunction(x):
    if x == 'close addMemberFrame':
        addMemberFrame.destroy()


# this function builds the addmember frame
def addMember():
    global addMemberFrame
    addMemberFrame = Frame(mainframe, bg='#c8dbd5', bd=5)
    addMemberFrame.place(rely=0.27, relx=0.05, relheight=0.6, relwidth=0.7)

    message = Label(addMemberFrame, text='Fill the form to add new member', font=('', 20), bg='#c8dbd5')
    message.place(relx=0.02, rely=0.05, relheight=0.08, relwidth=0.88)

    firstName = Label(addMemberFrame, text='First Name', bg='#c8dbd5', font=('', 20))
    firstName.place(rely=0.3, relx=0.01, relheight=0.1, relwidth=0.3)

    global firstNameEntry
    firstNameEntry = Entry(addMemberFrame, bg='white', font=('', 20), bd=3)
    firstNameEntry.place(relx=0.33, rely=0.3, relheight=0.1, relwidth=0.6)

    lastName = Label(addMemberFrame, text='Last Name', bg='#c8dbd5', font=('', 20))
    lastName.place(rely=0.5, relx=0.01, relheight=0.1, relwidth=0.3)

    global lastNameEntry
    lastNameEntry = Entry(addMemberFrame, bg='white', font=('', 20), bd=3)
    lastNameEntry.place(relx=0.33, rely=0.5, relheight=0.1, relwidth=0.6)

    global addMemberSave
    addMemberSave = Button(addMemberFrame, text='SAVE', bg='grey', bd=4, fg='white', font=('', 20),
                           command=lambda x=members: addMemberSafe(x))
    addMemberSave.place(relx=0.17, rely=0.7, relwidth=0.2, relheight=0.15)

    global addMemberExit
    addMemberExit = Button(addMemberFrame, text='EXIT', bg='red', bd=4, fg='white', font=('', 20),
                           command=lambda x='close addMemberFrame': exitFunction(x))
    addMemberExit.place(relx=0.6, rely=0.7, relwidth=0.2, relheight=0.15)


# this function adds more members to the member drop down menu
def addMemberSafe(x):
    name = firstNameEntry.get() + ' ' + lastNameEntry.get()
    x.append(name)  # add new name to member list x in this scope
    firstNameEntry.delete(0, END)
    lastNameEntry.delete(0, END)
    file1=open('MemberList.txt','a+')
    file1.write('\n'+name)
    path = 'Report'+'/'+ name + '.' + 'txt'#creating path variable for file name.txt
    open(path, 'at')#creating file: name.txt inside the Report folder
    file1.close()
    memberCombo(x)

    print(name)


# this function closes the form used to edit transactions
def closeForm():
    form.destroy()


# this function edits up to the last five transactions for the person selected.
def editForm(nameToEdit):
    print(nameToEdit)#debugger
    global form, formExit
    submit.destroy()  # this is to close the submit button
    closeTransactionDrop()  # this closes the combo drop box with the name from which we can edit
    tips = """
  Form on left shows up to
  last five transactions for today.
  Do the edits where needed.
  Contact tech support for
  older edits. Click submit
  when finished.
  """
    form = Frame(mainframe, bg='black', bd=3)  # this creates a frame in which we shall put our forms
    form.place(relx=0.02, rely=0.27, relwidth=0.95, relheight=0.71)

    formExit = Button(form, text='X', bg='red', fg='white', bd=2, font=('', 20),
                      command=closeForm)  # this is the small red exit button at the top right of frame
    formExit.place(relx=0.95, rely=0.0040, relheight=0.07, relwidth=0.05)

    dataframe = Frame(form, bg='#bcc8cc', bd=4)  # the two columns of forms, and submit and close button are in this frame
    dataframe.place(relx=0.009, rely=0.15, relwidth=0.65, relheight=0.850)

    amountEntry1=Entry(dataframe, bg='white', font=('', 15), )
    amountEntry1.place(relx=0.01, rely=0.01, relwidth=0.45, relheight=0.1)

    amountEntry2=Entry(dataframe, bg='white', font=('', 15), )
    amountEntry2.place(relx=0.01, rely=0.18, relwidth=0.45, relheight=0.1)

    amountEntry3 = Entry(dataframe, bg='white', font=('', 15), )
    amountEntry3.place(relx=0.01, rely=0.35, relwidth=0.45, relheight=0.1)

    amountEntry4 = Entry(dataframe, bg='white', font=('', 15), )
    amountEntry4.place(relx=0.01, rely=0.52, relwidth=0.45, relheight=0.1)

    amountEntry5 = Entry(dataframe, bg='white', font=('', 15), )
    amountEntry5.place(relx=0.01, rely=0.69, relwidth=0.45, relheight=0.1)

    
    #purposeBox1Variable=StringVar() i no longer use this because for some reason i dont get expected output
    purposeBox1 = ttk.Combobox(dataframe, background='white',font=('',15),state='readonly')
    purposeBox1['values'] = purpose
    purposeBox1.current(0)
    purposeBox1.place(relx=0.48, rely=0.01, relwidth=0.45, relheight=0.1)
    
    #purposeVariable2 = StringVar()
    purposeBox2 = ttk.Combobox(dataframe, background='white',font=('',15),state='readonly')
    purposeBox2['values']=purpose
    purposeBox2.current(1)
    purposeBox2.place(relx=0.48, rely=0.18, relwidth=0.45, relheight=0.1)
    
    purposeBox3 = ttk.Combobox(dataframe, background='white',font=('',15),state='readonly')
    purposeBox3['values']=purpose
    purposeBox3.current(1)
    purposeBox3.place(relx=0.48, rely=0.35, relwidth=0.45, relheight=0.1)
    
    purposeBox4 = ttk.Combobox(dataframe, background='white',font=('',15),state='readonly')
    purposeBox4['values']=purpose
    purposeBox4.current(1)
    purposeBox4.place(relx=0.48, rely=0.52, relwidth=0.45, relheight=0.1)
    
    purposeBox5 = ttk.Combobox(dataframe, background='white',font=('',15),state='readonly')
    purposeBox5['values']=purpose
    purposeBox5.current(1)
    purposeBox5.place(relx=0.48, rely=0.69, relwidth=0.45, relheight=0.1)
    
    



    notesFrame = Frame(form, bg='#e0dede')  # this frame will hold the text box for notes
    notesFrame.place(relx=0.665, rely=0.50, relwidth=0.33, relheight=0.50)

    notesHeading = Label(notesFrame, text='*** Notes ***', fg='black',
                         font=('', 20))  # this is the heading for that textbox
    notesHeading.place(relx=0.01, rely=0.01, relwidth=0.99, relheight=0.15)

    commentBox = Text(notesFrame, fg='black', font=('', 12), bd=3)  # this is the textbox for making notes
    commentBox.place(relx=0.01, rely=0.17, relwidth=0.99, relheight=0.84)

    tipsFrame = Frame(form, bd=1)  # the frame in which tips on the form will be
    tipsFrame.place(relx=0.665, rely=0.15, relwidth=0.33, relheight=0.345)

    formGuide = Label(tipsFrame, fg='black', bg='white', font=('', 10), bd=1,
                      text=tips)  # this label guides the user on how to fill form
    formGuide.place(relx=0.01, rely=0.17, relwidth=0.99, relheight=0.80)

    tipsTitle = Label(tipsFrame, text='*** Tips ***', fg='black', bg='#dcdfe3', font=('', 17))
    tipsTitle.place(relx=0.0, rely=0.0, relwidth=1, relheight=.20)
    
    #the submit and close button of the form to edit transactions. Also invokes dataCollector()
    formSave = Button(dataframe, text='Submit and Close', bg='#dcdfe3', fg='black', bd=4, font=('', 16),command=lambda x='Submit and Close':dataCollector(x))
    formSave.place(relx=0.30, rely=0.84, relwidth=0.43, relheight=0.15)
    
    formHeadingAmount=Label(form,text='Donated Amount',fg='white',bg='black',font=('',18))
    formHeadingAmount.place(relx=0.01,rely=0.05,relwidth=0.30,relheight=0.1)
    
    formHeadingPurpose=Label(form,text='Purpose',bg='black',fg='white',font=('',18))
    formHeadingPurpose.place(relx=0.27,rely=0.05,relwidth=0.27,relheight=0.1)
    
    # lastName=Label(form,text='Samari'+',',bg='black',fg='white',font=('',18))
    # lastName.place(relx=0.70,rely=0.01,relwidth=0.23,relheight=0.05)
    
    # firstName=Label(form,text='Godwill',bg='black',fg='white',font=('',18))
    # firstName.place(relx=0.70,rely=0.08,relwidth=0.23,relheight=0.05)
    
    name=Label(form,text=nameToEdit,fg='white',bg='black',font=('',18))
    name.place(relx=0.60,rely=0.05,relwidth=0.30,relheight=0.1)


# this function is to edit a transaction
def editTransaction(memberList):
    global editDropVariable, editTransactionBox, closeEditDrop, submit
    #editDropVariable = StringVar()
    #editDropVariable.set('Godwill Samari')
    editTransactionBox = ttk.Combobox(mainframe, background='white',font=('', 15))
    editTransactionBox['values']=memberList
    editTransactionBox.current(1)
    closeEditDrop = Button(mainframe, text='X', bg='red', fg='white', font=('', 17), command=closeTransactionDrop)
    closeEditDrop.place(relx=0.675, rely=0.257, relwidth=0.07, relheight=0.05)
    editTransactionBox.place(relx=0.34, rely=0.257, relwidth=0.32, relheight=0.05)
    submit = Button(mainframe, text='Submit Name', font=('', 20), fg='white', bg='grey', bd=4, command=lambda : editForm(editTransactionBox.get()))
    submit.place(relx=0.34, rely=0.32, relwidth=0.32, relheight=0.1)


# this function is to close both the combo drop box and the close button next to it
# that both appear when the Edit Transaction button is clicked.
def closeTransactionDrop():
    editTransactionBox.destroy()
    closeEditDrop.destroy()
    submit.destroy()


g = datetime.date.today()
root = Tk()
root.title('JESUS TABENACLE FINANCES. Call 919 519 1792 for technical support')

#the list of members is read from a text file called MemberList.txt
members=[]
stream=open('MemberList.txt','rt')
name=stream.readline()
while name!='':
  name=name.replace('\n','')#this is to remove the new line character automatically added by readline()
  members.append(name)
  path='Report' +'/'+ name +'.'+'txt' #this is the path variable to the file name.txt found in Report
  file1 = open(path,'a+')# creating file name.txt inside Report
  file1.close()
  name=stream.readline()
stream.close()

# this is the default donation set
purpose = ['Offerings',
           'Tithes',
           'Building Fund',
           'Sunday School',
           'Pastor',
           'Guest Minister',
           'Unspecified',
           'Special Seed']

method = ['Zelle','CashApp','Check','Cash','PayPal','Venmo','Money Oder']

canvas = Canvas(root, height=550, width=760, bg='black')
canvas.pack()
mainframe = Frame(canvas, bg='#b7cae8')
mainframe.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

dateTitle = Label(mainframe, text=str(g.month)+'-'+str(g.day)+'-'+str(g.year), font=('', 10), bg='#b7cae8', fg='black')
dateTitle.place(relx=0.78, rely=0.001, relwidth=0.2, relheight=0.03)

month = ['Jan','Feb','Mar','Apl','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
monthVariable = StringVar()
monthVariable.set('Jan')
monthBox = ttk.Combobox(mainframe, textvariable=monthVariable, font=('', 10), background='white', values=month,state='readonly')
monthBox.place(relx=0.81, rely=0.035, relwidth=0.08, relheight=0.033)


dayVariable = StringVar()
dayVariable.set('Jan')
dayBox = ttk.Combobox(mainframe, textvariable=dayVariable, font=('', 10), background='white', values=month,state='readonly')
dayBox.place(relx=0.895, rely=0.035, relwidth=0.08, relheight=0.033)













memberLabel = Label(mainframe, text='Select Donor         ', font=('', 15), bg='#b7cae8', fg='black')
memberLabel.place(relx=0.01, rely=0.01, relwidth=0.32, relheight=0.05)

amountLabel = Label(mainframe, text='Amount   ', font=('', 15), bg='#b7cae8', fg='black')
amountLabel.place(relx=0.23, rely=0.01, relwidth=0.25, relheight=0.05)

methodLabel = Label(mainframe,text='Method',font=('',15),bg='#b7cae8',fg='black')
methodLabel.place(relx=0.39,rely=0.01,relwidth=0.25,relheight=0.05)

methodBoxVar = methodVariable = StringVar()
methodBoxVar.set('Zelle')
methodBox = ttk.Combobox(mainframe,textvariable=methodBoxVar, font=('', 15), background='white', values=method,state='readonly')
methodBox.place(relx=0.44,rely=0.07,relwidth=0.15,relheight=0.05)


purposeLabel = Label(mainframe, text='Purpose', font=('', 15), bg='#b7cae8', fg='black')
purposeLabel.place(relx=0.6, rely=0.01, relwidth=0.15, relheight=0.05)


Amount = Entry(mainframe, bg='white', font=('', 15), )#amount donated
Amount.place(relx=0.28, rely=0.07, relwidth=0.15, relheight=0.05)

#this is to select the puropse of the donation
purposeBoxVariable = StringVar()
purposeBoxVariable.set('Offerings')
purposeBox = ttk.Combobox(mainframe, textvariable=purposeBoxVariable, font=('', 15), background='white', values=purpose,state='readonly')
purposeBox.place(relx=0.6, rely=0.07, relwidth=0.2, relheight=0.05)

#the save button on the main page. Also invokes dataCollector()
saveButton = Button(mainframe, text='SAVE', fg='white', bg='grey', font=('', 17), bd=3,command=lambda x='Save':dataCollector(x))
saveButton.place(relx=0.81, rely=0.07, relwidth=0.18, relheight=0.05)

addButton = Button(mainframe, text='Add Member', font=('', 18), bg='grey', fg='white', bd=4, command=addMember)
addButton.place(relx=0.07, rely=0.15, relheight=0.1, relwidth=0.25)

editButton = Button(mainframe, text='Edit a Transaction', font=('', 17), fg='white', bg='grey', bd=4,
                    command=lambda x=members: editTransaction(x))
editButton.place(relx=0.34, rely=0.15, relwidth=0.32, relheight=0.1)

summary = Button(mainframe,text='View Summary',font=('',17),fg='white',bg='grey',bd=4)
summary.place(relx=0.685, rely=0.15, relwidth=0.25, relheight=0.1)

# this section is modular because as we add members to the member dropdown, we shall constantly update it
def memberCombo(memberList):
    global memberBox, memberBoxVariable
    memberBoxVariable = StringVar()  # this is the variable for items in the drop down
    memberBoxVariable.set('Godwill Samari')  # Godwill will alway be the default name
    memberBox = ttk.Combobox(mainframe, textvariable=memberBoxVariable, font=('', 15), background='white',
                             values=memberList,state='readonly')
    memberBox.place(relx=0.01, rely=0.07, relwidth=0.25, relheight=0.05)
    root.option_add('*TCombobox*Listbox.font', ('', 15))


memberCombo(members)  # this will only run one time, and it will be the first time the combo box is made
root.mainloop()




#THESE ARE THE CURRENT BUGGS IN THIS CODE
# 1. I get PY_VAR2 instead of the name of the person whose transactions are being edited when 
# 'Submit Name' button is pressed. That is under Edit Transactions
# PARTIALLY SOLVED. the reason was because i was not using the get() methode. The default still
# remains as the name i passed in edidDropVariable.set(), rather than my selection


# 2. the default Donated Amount, and Purpose are not being shown in the edit form.
# Thats after Submit Name button is pressed

