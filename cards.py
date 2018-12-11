from random import randint

suits = ["Hearts", "Diamonds", "Spade", "Clubs"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "k", "A"]


class Card:
  def __init__(self, suit, value):
    self.suit = suit
    self.value = value
  
  
  
  
class Deck:
  def __init__(self):
    self.cards = []
    self.hands = {}
    
  def createDeck(self):
    for i in range(len(values)):
      for j in range(len(suits)):
        self.cards.append(Card(suits[j], values[i]))
    return self.cards
    
  def shuffle(self, newDeck, deckLength):
    if len(newDeck) < deckLength:
      card = self.cards[randint(0, len(self.cards)-1)]
      newDeck.append(card)
      self.cards.remove(card)
      return self.shuffle(newDeck, deckLength)
    else:
      self.cards = newDeck
      return self.cards

  def get(self, attr):
    values = []
    for each in self.cards:
      if attr == "values":
        values.append(each.value)
      else:
        values.append(each.suit)
    return values
    
  def draw(self):
    for each in self.cards:
      print each.value + " of " + each.suit

 
deck = Deck()
deck.createDeck()
deck.shuffle([], 52)


hand = deck.cards[:5]
for each in hand:
  print each.value, each.suit


   
    
  
