
# coding: utf-8

# In[45]:

from itertools import chain

board_state = [['a0', 'a1', 'a2'], 
               ['b0', 'b1', 'b2'], 
               ['c0', 'c1', 'c2']]

# TODO: replace test display with images
board_display = ['a0',' | ','a1',' | ','a2','\n',
                 '------------','\n',
                 'b0',' | ','b1',' | ','b2','\n',
                 '------------','\n',
                 'c0',' | ','c1',' | ','c2']

win_states = []
for i in range(3):
    win_states.append(board_state[i])
    win_states.append([row[i] for row in board_state])
    if i==0:
        win_states.append([board_state[i+j][i+j] for j in range(3)])
        win_states.append([board_state[i+j][2-j] for j in range(3)])
        
def update_board(player, mark):
    global board_state, board_display, win_states, player_1
    position = input('Player {}, place your {}: '.format(player,mark))
    if not position in chain(*board_state):
        print('Oops! Invalid input.')
        update_board(player, mark)
    board_state = [[board_state[i][j] if board_state[i][j] != position else mark 
                    for j in range(3)] 
                   for i in range(3)]
    board_display = [e if e != position else ' '+mark for e in board_display]
    win_states = [[win_states[i][j] if win_states[i][j] != position else mark 
                    for j in range(3)] 
                  for i in range(len(win_states))]
    player_1 = not player_1

print(''.join(board_display))

player_1 = True
# check that no win conditions have been met 
while not ((['X','X','X'] or ['O','O','O']) in win_states or 
           all([all([board_state[i][j] in ['X','O'] 
                 for i in range(3)]) 
                for j in range(3)])):
    if player_1:
        update_board(1,'X')   
    else:
        update_board(2,'O')
        
    print(''.join(board_display))

        
if ['X','X','X'] in win_states:
    print('Player 1 wins!')
else:
    print('Player 2 wins!')
    


# In[44]:

[[board_state[i][j] in ['X','O'] 
                 for i in range(3)] 
                for j in range(3)]


# In[41]:

board_state


# In[ ]:



