from processing import *
from random import randint, shuffle
from time import sleep


WIDTH = 400
HEIGHT = 400
colors = ["red", "green", "blue", "yellow"]


def setup():
  size(WIDTH, HEIGHT)
  frameRate(30)



def addText(string, x,y, size):
  textSize(size)
  fill(0)
  return text(string, x,y)


  
class Card:
  def __init__(self, x,y, color):
    self.x = x
    self.y = y
    self.width = 50
    self.height = 75
    self.color = color
    self.flipped = True
    
  def draw(self):
    if self.flipped:
      if self.color == "blue":
        fill(0,0,255)
      elif self.color == "green":
        fill(0,255,0)
      elif self.color == "red":
        fill(255,0,0)
      elif self.color == "yellow":
        fill(255,255,0)
      else:
        fill(0)
    else:
      fill(255,255,255)
    
    rect(self.x, self.y+20, self.width, self.height)
    
    
  def toggle(self):
    if self.press():
      if self.flipped:
        self.flipped = False
      else:
        self.flipped = True
      
  def press(self):
    return mouse.x > self.x and mouse.x < self.x+self.width and mouse.y > self.y and mouse.y < self.y + self.height   
     
  
class Grid:
  def __init__(self, rowSize, colSize):
    self.rowSize = rowSize
    self.colSize = colSize
    self.grid = []
    self.scale = 100
    self.count = 0
    self.colors = []
    self.selectColors()
    self.createGrid()
    
    
  def selectColors(self):
    for i in range(self.rowSize):
      for color in colors:
        self.colors.append(color)
    shuffle(self.colors)
    
    
  def createGrid(self):
    for row in range(self.rowSize):
      for col in range(self.colSize):
        self.grid.append(Card(row*self.scale,col*self.scale, "white" ))
    for i in range(len(self.colors)):
      self.grid[i].color = self.colors[i]
    
  def draw(self):
    for i in range(len(self.grid)):
      self.grid[i].draw()
      
      
  def reset(self):
    for i in range(len(self.grid)):
      self.grid[i].flipped = False
      
  def checkMatch(self):
    match = []
    for card in self.grid:
      if card.flipped:
        match.append(card)
        
    if len(match) > 1:
      if match[0].color == match[1].color:
        self.grid.remove(match[0])
        self.grid.remove(match[1])
      
    
  
  def update(self):
    for i in range(len(self.grid)):
      self.grid[i].toggle()
      if self.grid[i].flipped:
        self.count += 1
        
      
    if self.count > 3:
      self.checkMatch()
      self.reset()
      self.count = 0
     
      
def mouseClicked():
  grid.update()
  
  
  
  

grid = Grid(4,4)
 
def update():
  background(180, 221, 224)
  grid.draw()
  if len(grid.grid) < 1:
    addText("You win", 100,100, 24)
  else:
    pass
 
  
draw = update 
run()
