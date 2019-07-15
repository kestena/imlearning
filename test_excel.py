#import openpyxl
import os
import glob

#print current folder
print (os.path)

#check if there is an excel file and create a list 
#so that the user can request which file he wants
def which_file ():
    empty_xls_list = []
    for file in glob.glob("*.xls*"):
        empty_xls_list.append(file)
    print ("-"*20)
    print ("File Name")
    print ("-"*20)
    x = 1
    for item in empty_xls_list:
        print (str(x) +"." + " " + item)
        x+=1
        print ("="*20)
        
    #print (empty_xls_list, end = " ")
    
which_file()
