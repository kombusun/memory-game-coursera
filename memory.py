# My final implementation of the card game Memory for the Coursera Class 
# An Introduction to Interactive Programming in Python

import simplegui
import random

list1 = range(8)
list2 = range(8)
cards = list1 + list2
i = range(0,16)
exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
turns = 0

# helper function to initialize globals
def new_game():
    global state, exposed  
    state = 0
    exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    random.shuffle(cards)
    return cards

def mouseclick(pos):
    global state, turns, first_card, first_card_i, second_card, second_card_i
    # Get card_index of clicked card
    card_index = pos[0] // 50
    
    # Only work with hidden cards
    if not exposed[card_index]:
    
        if state == 0:
            first_card_i = pos[0]//50
            first_card = str(cards[pos[0]//50])
            exposed[first_card_i] = True
            state = 1
            turns += 1
            return pos
        elif state == 1:
            second_card_i = pos[0]//50
            second_card = str(cards[pos[0]//50])
            exposed[pos[0]//50] = True
            state = 2
            label.set_text("Turns = " + str(turns))
            return pos
        else:
            if first_card != second_card:
                exposed[first_card_i] = False
                exposed[second_card_i] = False
                exposed[pos[0]//50] = True
                first_card_i = pos[0]//50
                first_card = str(cards[pos[0]//50])          
                state = 1
                turns += 1
                return pos
            elif first_card == second_card:
                first_card_i = pos[0]//50
                first_card = str(cards[pos[0]//50])
                exposed[first_card_i] = True            
                exposed[second_card_i] = True
                state = 1
                turns += 1
                return pos
                             
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for card_index in range(len(cards)):
        card_pos = 50 * card_index + 10
        canvas.draw_text(str(cards[card_index]), (card_pos, 70), 50, 'White')    
    for i in range(len(exposed)):
        if exposed[i] == False:
            card_pos = 50 * i + 25
            canvas.draw_line((card_pos, 0), (card_pos, 100), 48, 'Green')       
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turns))


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
