import ast #this is the module that converts stringed list back to list type
#this moduke will solve the problem of summarizing from a data logger file
def writeBannar(name):
    path='Report' +'/'+ name +'.'+'txt' #building path variable for the particular customer file
    stream = open(path,'w')#open in write mode so as to wipe file clean at start
    stream.write(70*'*'+'\n')
    stream.close()
    
    stream = open(path,'a+')
    stream.write('RCCG-Jesus Tabernacle.  '+name+'\n')
    stream.write(70*'*'+'\n')
    stream.write('AMOUNT'+ 4*'\t' + 'PURPOSE' + 4*'\t' + 'DATE' + '\n')
    stream.close()
    return path






def summary(name):
    transactions = []
    file = open('dataLog.txt')
    lines = [line.strip() for line in file]#this is a list of all transactions
    file.close()
    print(lines)

    for record in lines:
        record2 = ast.literal_eval(record)#to convert string type back to list
        for item in record2:
            if item == name:
                transactions.append(record2)
    path = writeBannar(name)#writeBannar()will return file path
    print(transactions)#this was for testing

    total = 0
    file = open(path,'a')
    for record in transactions:
        total = total + float(record[1])#find the total contribution
        file.write(f"{str(record[1]):<25}     {record[3]:<25}     {record[4]}\n")
        print(f"{str(record[1]):<25}     {record[3]:<25}     {record[4]}\n")
    file.write('YTD Total = $')
    file.write(str(total))
    file.close()
                                                                        
