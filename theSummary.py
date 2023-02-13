import ast #this is the module that converts stringed list back to list type
#this moduke will solve the problem of summarizing from a data logger file
def writeBannar(name):
    path='Report' +'/'+ name +'.'+'txt' #building path variable for the particular customer file
    stream = open(path,'a+')
    stream.write(40*'*'+'\n')
    stream.write(name+'\n')
    stream.write(40*'-'+'\n')
    stream.write('AMOUNT'+ 2*'\t' + 'PURPOSE' + 2*'\t' + 'DATE' + '\n')
    stream.close()






def summary(name):
    transactions = []
    file = open('dataLog.txt')
    lines = [line.strip() for line in file]#this is a list of all transactions
    file.close()
    print(lines)

    for record in lines:
        record2 = ast.literal_eval(record)#to conver string type back to list
        for item in record2:
            if item == name:
                transactions.append(record2)
    writeBannar(name)
    print(transactions)
