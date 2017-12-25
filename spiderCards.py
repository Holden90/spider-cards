#!/bin/env python
import random
import sys

#define a card class
class card(object):
    def __init__( self, points, color, state ):
        self.points = points
        self.color = color
        self.state = state
    #what to show   
        self.display = "["+self.color+"]"+self.points if self.state else '*'
#function to create a column        
def init_columns(num, card_pool):
    col = []
    for i in range(num):
        card = random.choice(card_pool)
        col.append(card)
        card_pool.remove(card)
    return col    
        
#initiate the 104 cards pool
def create_card_pool():
    card_pool = []
    for i in range(8):
        for n in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            card_pool.append(card(n, 'black', False ))
    return card_pool

#start the game with only one card showing at each column's bottom
def display(top_cols, btm_cols):
    row_display = []
    matrix_height = max([len(n) for n in top_cols])
    for i in range(matrix_height):
        row_string = ""
        for n in top_cols:
            row_string += n[i].display+"    " if i < len(n) else " "+"    "
        row_display.append(row_string)
    for x in row_display:
        print x
    print "     "*10
    print "{0:>46s}".format("%d decks left" % len(btm_cols))

def main():
    top_cols = []
    btm_cols = []
    card_pool = create_card_pool()
    #create the top 10 columns
    for i in range(10):
        if i <4:
            top_cols.append(init_columns(6, card_pool))
        else:
            top_cols.append(init_columns(5, card_pool))
    #create the bottom 5 decks
    for i in range(5):
        btm_cols.append(init_columns(10, card_pool))
    display(top_cols,btm_cols)
    
    
    
        
        
if __name__ == "__main__":
    main()
