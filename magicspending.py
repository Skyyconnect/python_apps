
collection = {}
total = 0

def price():
    try:
        return float(raw_input("$:"))
    except:
        print("Price was not entered. Try again")

def sold(amount):
    try:
        total = (total- amount)
        return total
    except:
        print("Something went wrong. Try again.")
def card():
    try: 
        return raw_input("card:")
    except:
        print ("Card was not entered. Try again.")

def addTo(card, price):
    global total
    try:
        total += price
        collection[card] = price
        return collection
    except:
        print("Could not add to collection. Try again.")

def File(fileName, types):
    try:
        return open(fileName, types)
    except:
        print ("Error: file not made.")
        return False
        
def writer(fileName, content, types):#types: "w"-> writing(exiting file will be erased); "a"--> opens file for appending(data append); "r+" --> open for reading and                                           writing;"r" --> defualt.
    try:
        with File(fileName,types) as out:
            out.write(content + '\n')
        return True
    except:
        print ("Error: file writer failed.")
        return False

    
def ask(text):
    return(float(input(text)))
    
def catch(a):
    try:
        return a
    except:
        print("Error:Something went wrong. Try again.")
        return False

on = True

while on:
    into = raw_input("**>")
    if into == "add":
        addTo(card(), price())
    if into == "reset":
        collectin = {}
        total = 0
    if into == "collection":
        print (collection)
    if into == "log":
        writer("magicLog.txt", "Collection added: "+ str(collection)+str(total), "a")
            
    
    if into == "stop":
        print ("Good-Bye")
        on = False
        break
    print ("total: " + str(total))
