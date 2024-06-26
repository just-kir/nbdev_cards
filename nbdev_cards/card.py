# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_card.ipynb.

# %% auto 0
__all__ = ['suits', 'ranks', 'Card']

# %% ../nbs/00_card.ipynb 3
from fastcore.utils import *

# %% ../nbs/00_card.ipynb 4
suits = "♠♥♦♣"
ranks = [None, "A"] + [str(i) for i in range(2, 11)] + ["J", "Q", "K"]

# %% ../nbs/00_card.ipynb 9
class Card():
  "A playing card created by passing `rank` from `ranks` and `suit` from `suits`."
  def __init__(self,
               suit:int, # 0-3 range
               rank:int, # 0-13 range
              ):
    self.suit = suit 
    self.rank = rank
  def __str__(self):
    return f"{ranks[self.rank]}{suits[self.suit]}"
  __repr__ = __str__


# %% ../nbs/00_card.ipynb 13
@patch
def __eq__(self:Card, other:Card):
  return self.suit == other.suit and self.rank == other.rank

# %% ../nbs/00_card.ipynb 15
@patch
def __lt__(self:Card, other:Card):
  return (self.suit, self.rank) < (other.suit, other.rank)

# %% ../nbs/00_card.ipynb 17
@patch
def __gt__(self:Card, other:Card):
  return (self.suit, self.rank) > (other.suit, other.rank)
