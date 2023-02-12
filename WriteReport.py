def writer(lines,data,path):
    lastLine = lines[len(lines)-1]#get last line from list of all lines from file
    print('the last line is : ',lastLine)#testing
    amount = lastLine[13:len(lastLine)]#extract the numerical string from last line
    amount = float(amount)#convert it to float for arithmetics
    total = amount+float(data[1])#find the new total
    print(round(total,2))
