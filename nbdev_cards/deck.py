# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_deck.ipynb.

# %% auto 0
__all__ = ['Deck', 'draw_n']

# %% ../nbs/01_deck.ipynb 3
from fastcore.utils import *
from .card import *
import random

# %% ../nbs/01_deck.ipynb 4
class Deck:
  "A deck of 52 cards."
  def __init__(self):
    self.cards = [Card(rank, suit) for suit in range(1, 14) for rank in range(4)]
  def __len__(self):
    return len(self.cards)
  def __contains__(self, card):
    return card in self.cards
  def __str__(self):
    return '; '.join(map(str, self.cards))
  __repr__ = __str__
  
  def shuffle(self):
    "Shuffle the deck."
    random.shuffle(self.cards)
  

# %% ../nbs/01_deck.ipynb 9
@patch
def pop(self:Deck, 
        idx:int=-1
        ) -> Card:
  "Remove top card from the deck"
  return self.cards.pop(idx)

# %% ../nbs/01_deck.ipynb 11
@patch
def remove(self:Deck,
           card:Card
           ) -> None:
  "Remove a `Card` from the deck"
  self.cards.remove(card)
  

# %% ../nbs/01_deck.ipynb 14
def draw_n(n:int, # number of cards to draw
           replace:bool=True # whether to replace the drawn cards
           ) -> list:
  "Draw `n` cards from the deck with replacement iif `replace` is True"
  d = Deck()
  d.shuffle()
  if replace:
    return [d.cards[random.choice(range(len(d.cards)))] for _ in range(n)]
  else:
    return d.cards[:n]
