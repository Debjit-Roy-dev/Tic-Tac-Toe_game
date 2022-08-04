def display_board(board):
    print('\n'*100)
    print('  |  |')
    print(board[7]+' | '+board[8]+'| '+board[9])
    print('  |  |')
    print('___________')
    print('  |  |')
    print(board[4] + ' | ' + board[5] + '| ' + board[6])
    print('  |  |')
    print('___________')
    print('  |  |')
    print(board[1] + ' | ' + board[2] + '| ' + board[3])
    print('  |  |')


def player_input():
    marker=''
    while marker !='X' and marker !='O':
        marker=input('player 1 choose X or O:  ').upper()
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')


def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,mark):
    return (board[1]== mark and board[2]==mark and board[3]== mark) or (board[4]==mark and board[5]==mark and board[6]== mark) or (board[7]==mark and board[8]==mark and board[9]== mark)or (board[1] == mark and board[4] == mark and board[7] == mark) or (board[2]==mark and board[5]==mark and board[8]== mark) or (board[3]==mark and board[6]==mark and board[9]== mark) or (board[3] == mark and board[5] == mark and board[7] == mark) or (board[1]==mark and board[5]==mark and board[9]== mark)

import random
def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return 'player 1'
    else:
        return 'player 2'


def space_check(board,position):
    return board[position]==' '


def full_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position=0
    while position  not in range(1,10) or not space_check(board,position):
        position=int(input('choose a position(1-9):  '))
    return position

def replay():
    choice=input("play again?enter (y/n)")
    return choice=='y'


#main function

#1 while loop to keep playing the game


print("welcome to tic tac toe")
while True:
    #play the game

    ## set board  who first choose marker x,o
    the_board=[' ']*10
    player_1_marker,player_2_marker=player_input()

    turn=choose_first()
    print(turn+' will go 1st')

    play_game=input('ready to play?(y/n)')

    if play_game=='y':
        game_on= True
    else:
        game_on= False

    ##game play

    while game_on:
        if turn=='player 1':
            #show board
            display_board(the_board)

             #choose a position
            position=player_choice(the_board)
            #place the marker on the position
            place_marker(the_board,player_1_marker,position)

            #check if they won
            if win_check(the_board,player_1_marker):
                display_board(the_board)
                print('player 1 has won...')
                game_on=False
            #check if tie
            else:
                if full_check(the_board):
                    display_board(the_board)
                    print('tie game!!!')
                    game_on=False
                else:
                    turn='player 2'
            #no tie and no win then next players turn
        else:
            # show board
            display_board(the_board)

            # choose a position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board, player_2_marker, position)

            # check if they won
            if win_check(the_board, player_2_marker):
                display_board(the_board)
                print('player 2 has won...')
                game_on = False
            # check if tie
            else:
                if full_check(the_board):
                    display_board(the_board)
                    print('tie game!!!')
                    game_on = False
                else:
                    turn = 'player 1'


    # 2 break while loop by replay()
    if not replay():
        break

