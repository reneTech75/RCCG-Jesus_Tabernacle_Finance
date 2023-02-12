import os
import WriteReport

def pageSetup(name,path):#this setup page sets up a blank page into the basic summary style.
    stream = open(path,'a+')
    stream.write(40*'*'+'\n')
    stream.write(name+'\n')
    stream.write(40*'-'+'\n')
    stream.write('AMOUNT'+ 2*'\t' + 'PURPOSE' + 2*'\t' + 'DATE' + '\n')
    #stream.write('YTD Total = $')#i have temporarily commented out this one while i figure out how to add amounts from the file
    lines = [line.strip() for line in stream]
    stream.close()
    print(lines)
    return lines

def dataCollector(data):
    #the next few lines get the data from data list into variables
    name = data[0]
    amount = data[1]
    purpose = data[3]
    date = data[4]

    #print(name)
    #print(amount)
    #print(purpose)
    #print(date)

    path='Report' +'/'+ name +'.'+'txt' #building path variable for the particular customer file

    #myFile = open(path, 'a+')
    #print(os.path.isfile(path))#this was during debugging to ensure that i properly constructed the path variable.
    #print(path)

    #myFile.write('this one na test')
    #myFile.close()
    
    print('start of test1')
    file = open(path)
    lines = [line.strip() for line in file]#this is a list of all line in the file without the new line character
    print(lines)#debug line
    file.close()
    print('end of test2')

    if(len(lines) < 4):#the basic setup page without any data should have 4 lines, ie a banner, customer name, another banner, and ytd total
        print('start of test3')
        lines = pageSetup(name,path)
    print(lines)
    lastLine = lines[len(lines)-1]#this extracts the content of the last line on file which is stored in list called lines
    print(lastLine)
    WriteReport.writer(lines,data,path)
    
