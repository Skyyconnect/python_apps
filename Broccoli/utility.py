from random import *
from sys import *
import os





def randNum(num):
    return randint(1, num)

def File(fileName, types):
    try:
        return open(fileName, types)
    except:
        print ("Error: file not made.")
        return False
        
def writer(fileName, content, types):#types: "w"-> writing(exiting file will be erased); "a"--> opens                                       file for appending(data append); "r+" --> open for reading and                                           writing;"r" --> defualt.
    try:
        with File(fileName,types) as out:
            out.write(content + '\n')
        return True
    except:
        print ("Error: file writer failed.")
        return False

def deleteFile(path):
    try:
        os.remove(name)
        return True
    except:
        print("Error: file not deleted.")
        return False
    
def deleteDirectory(path):
    try:
        os.rmdir(name)
        return True
    except:
        print("Error: directory not deleted.")
        return False
        
def ask(content):
    return input(content)

def log(data):
    writer(log, fileName,data)
    print("process was logged in temp")
    return True


def fileSize(filePath):
    return str(os.path.getsize(filePath))





    
        

        
    


    
    





