from random import randint,shuffle


card = ["[2]","[3]","[4]","[5]","[6]","[7]","[8]","[9]","[10]","[J]","[Q]","[K]","[A]",]
suit = ["Hearts", "Clubs", "Spades", "Diamonds"]
deck = []
class Cards:
  def __init__(self, deck):
    self.card = card
    self.suits = suit
    self.deck = deck 
  
  
  def makeDeck(self):
    self.deck = []
    for i in xrange(len(card)):
      for j in range(len(suit)):
        self.card = card[i]+ suit[j]
        self.deck.append(self.card)
    print len(self.deck)
    return self.deck
    
  def shuffler(self):
    return shuffle(self.deck)
    
cardDeck = Cards(deck)
cardDeck.makeDeck()
cardDeck.shuffler()
print cardDeck.deck
