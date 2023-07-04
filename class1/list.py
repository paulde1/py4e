filename = input("Enter file name: ")
filehandler = open(filename)
lst = list()

for line in filehandler:
    for line in filehandler:                    
        word= line.rstrip().split() 
        for element in word:        
            if element in lst:        
                continue           
            else :                    
                lst.append(element)    
lst.sort()                         
# print(lst)                        