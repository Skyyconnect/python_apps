from random import randint 
import cmath
import random
import math
from utility import *
from os import *





 
class Node(object):
    def __init__(self,name, data):
        self.data = data
        self.children = []
        self.temp = []
        self.stack= []
        self.database = {}
        self.name = name
        self.childEnd = len(self.children)-1
        
        
    def stats(self):
        print "******************"
        print "Node Name: " + self.name
        print "Children: " + str(self.children)
        print "Stack: "+ str(self.stack)
        print "Temp: " + str(self.temp)
        print "Database: "+ str(self.database)
        print "Data: "+ str(self.data)
        print "******************"
    def add(self, obj):
        self.children.append(obj)
        self.stack.append(obj)
        return self.children
    
    def remove(self, obj):
        self.children.remove(obj)
        return self.children
    
    def isMax(self, obj):
        if len(self.children) > 0:
            if obj >= self.children[self.childEnd]:
                self.temp.append(obj)     
            else:
                self.temp = []
        else:
            print "there are no node children"
    def empty(self, obj):
        if len(self.children) > 0:
            if obj >= self.children[self.childEnd]:
                self.stack.append(self.temp[0])
                self.temp = []
            else:
                self.stack =[]
                self.temp = []
        else:
            print "there are no node children"
        return self.children
    
    def FILO(self, obj):
        try:
            self.stack[0] = obj
        except:
            print "stack is broken"
            if len(self.stack) >0:
                try:
                    self.stack.remove(self.stack[len(self.stack)-1])
                except:
                    print "cannot remove from stack"
        return self.stack
    
    def save(self,obj, key):
        self.database[key] = obj
        return self.database
    
    def datas(self, data):
        self.data = data
        return self.data
    
    def destroy(self):
        self.temp = []
        self.stack = []
        print "system flushed"
    def isString(self, data):
        if isinstance(data, basestring):
            print "string"
            return ' '.join(format(x, 'b') for x in bytearray(data))
        else:
            return data


    

def omega(p,q):
    return cmath.exp((2.0*cmath.pi*1j *q)/p)
    
    
def fft(signal):
    n = len(signal)
    if n ==1:
        return signal
    else:
        Feven = fft([signal[i] for i in xrange(0,n,2)])
        Fodd = fft([signal[i] for i in xrange(1,n,2)])
        combined = [0]*n
        for m in xrange(n/2):
            combined[m]= Feven[m] + omega(n, -m)*Fodd[m]
            combined[m+n/2] = Feven[m] - omega(n, -m) *Fodd[m]
        return combined

    
def frequencyFilter(signal):
    for i in range(20000, len(signal)-20000):
        signal[i]= 0

'''def quick_sort(items):
        pivot_index = len(items) / 2
        smaller_items = []
        larger_items = []
        """ Implementation of quick sort """
        if len(items) > 1:
            pivot_index = len(items) / 2
            smaller_items = []
            larger_items = []

        for i, val in enumerate(items):
            if i != pivot_index:
                if val < items[pivot_index]:
                    smaller_items.append(val)
                else:
                    larger_items.append(val)

            quick_sort(smaller_items)
            quick_sort(larger_items)
            items[:] = smaller_items + [items[pivot_index]] + larger_items
        return items

      '''  
 

    

def dynamicTimeWarp(seqA, seqB, d = lambda x,y: abs(x-y)):
    # create the cost matrix
    numRows, numCols = len(seqA), len(seqB)
    cost = [[0 for _ in range(numCols)] for _ in range(numRows)]
 
    # initialize the first row and column
    cost[0][0] = d(seqA[0], seqB[0])
    for i in xrange(1, numRows):
        cost[i][0] = cost[i-1][0] + d(seqA[i], seqB[0])
 
    for j in xrange(1, numCols):
        cost[0][j] = cost[0][j-1] + d(seqA[0], seqB[j])
 
    # fill in the rest of the matrix
    for i in xrange(1, numRows):
        for j in xrange(1, numCols):
            choices = cost[i-1][j], cost[i][j-1], cost[i-1][j-1]
            cost[i][j] = min(choices) + d(seqA[i], seqB[j])
 
    for row in cost:
        for entry in row:
            print "%03d" % entry,
        print("")
    return cost[-1][-1]



#Helper Functions 
def stateMachine(node,data):

    states = {
    "addChild": node.add(data),
   # "sort": quick_sort(node.children),
    "temp": node.isMax(data),
    "save": node.save(data, node.children[node.childEnd]),
    "filo": node.FILO(data),
    "create Stack": node.empty(data),
    "stats": node.stats(),
    "destroy":node.destroy()



    }

    return states


def rand(num):
    return randint(0,num)

def array(item, n):
    for i in xrange(n):
        item.append(rand(i+1))
    return item

def ask(text):
    return raw_input(text)


def node(name, data):
    return Node(name, data)
    
def tester(node):
    commands = [ 
            "add",
           "remove",
            "save",
             "filo",
            "empty",
             "stop",
             "ismax",
             "destroy",
             "data",
             "info",
             "add random",
            "delete data ",
             "write",
             "data size"]
    n = 0
    while n<1:
        com = ask("data>")
        if com =="stop":
            n = 1
            break
        if com == "info":
            node.stats()
        if com == "add random":
            node.add(rand(100))
        if com == "write":
            writer("data.txt", node.data, "a")
        if com == "delete data":
            deleteFile("data.txt")
        if com == "data size":
            print fileSize("data.txt") + " bytes"
        if com == "command":
            for each in commands:
                print each
        else:
            stateMachine(node, com)

        

   #########################

system = []
node = Node("broccoli", array(system, 1))
print node.stats()
tester(node)

'''
# testing some of the fft stuff
print("___---___---__---__----_____----")
print fft([5,1,0,8])
print("___---___---__---__----_____----")

w = cmath.exp(2*cmath.pi*1j/8)
d = 4
print fft([w**(k*d) for k in range(20)])

print("___---___---__---__----_____----")
'''
#inputSignal = [x/2.0 + random.random()*0.1 for x in inputSignal]

