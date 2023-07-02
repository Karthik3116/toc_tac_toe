from tkinter import * 
import random
import time

root = Tk()
root.geometry("500x500")

fram1 = Frame(root,bg= "black")
fram1.pack()


turn = "X"
game_end = False

main_board = {1:"", 2:"", 3:"",
         4:"", 5:"", 6:"",
         7:"", 8:"", 9:""}

def update_board():
    for key in main_board.keys():
        all_buttons[key-1]["text"] = main_board[key]

def checkForWin(player):
    # rows
    if main_board[1] == main_board[2] and main_board[2] == main_board[3] and main_board[3] == player:
        return True
    
    elif main_board[4] == main_board[5] and main_board[5] == main_board[6] and main_board[6] == player:
        return True
    
    elif main_board[7] == main_board[8] and main_board[8] == main_board[9] and main_board[9] == player:
        return True

    # columns
    elif main_board[1] == main_board[4] and main_board[4] == main_board[7] and main_board[7] == player:
        return True
    
    elif main_board[2] == main_board[5] and main_board[5] == main_board[8] and main_board[8] == player:
        return True
    
    elif main_board[3] == main_board[6] and main_board[6] == main_board[9] and main_board[9] == player:
        return True
    
    # diagonals
    elif main_board[1] == main_board[5] and main_board[5] == main_board[9] and main_board[9] == player:
        return True
    
    elif main_board[3] == main_board[5] and main_board[5] == main_board[7] and main_board[7] == player:
        return True
    

    return False

def checkfordraw():
    for i in main_board.keys():
        if main_board[i] == "":
            return False
    
    return True


def check_empty(board):
    empty_cells = []
    for i in (board.keys()):
        if board[i] == "":
            empty_cells.append(i)

    return empty_cells


def minimax(board, ismaximizing):

    if checkForWin("O"):
        return 1
    if checkForWin("X"):
        return -1
    if checkfordraw():
        return 0

    if ismaximizing:
        best_score = -100
        bestmove = 0

        empty_cell = check_empty(main_board)
        for one in empty_cell:
            main_board[one] = "O"
            score = minimax(main_board, False)
            main_board[one] = ""
            if score > best_score:
                best_score = score

        return best_score

    elif not ismaximizing:
        
        best_score = 100
        

        empty_cell = check_empty(main_board)
        for one in empty_cell:
            main_board[one] = "X"
            score = minimax(main_board, True)
            main_board[one] = ""
            if score < best_score:
                best_score = score

        return best_score

def comp_move():
    best_score = -100
    bestmove = 0

    empty_cell = check_empty(main_board)
    for one in empty_cell:
        main_board[one] = "O"
        score = minimax(main_board, False)
        main_board[one] = ""
        if score > best_score:
            best_score = score
            bestmove = one

    main_board[bestmove] = "O"


def restart_game():
    global game_end,turn 
    turn = "X"
    game_end = False
    for one in all_buttons:
        one["text"] = ""
    for i in main_board.keys():
        main_board[i] = ""


          
def play(event):
    global turn, game_end,main_board

    if game_end:
        return

    button = event.widget
    number = str(button)
    clicked = number[-1]
    if clicked == 'n':
        clicked = 1
    else:
        clicked = int(clicked)

    if button["text"] == "":
        if turn == 'X':
            button["text"] = "X"
            main_board[clicked] = button["text"]
            if checkForWin(turn):
                print("X WINS")
                game_end = True
            elif checkfordraw():
                print("DRAW")
                game_end = True
            else:
                turn = 'O'
                comp_move()
                update_board()
                if checkForWin(turn):
                    print("O WINS")
                    game_end = True
                elif checkfordraw():
                    print("DRAW")
                    game_end = True
                turn = "X"
            print(main_board)
        else:
            
            button = event.widget
            button["text"] = "O"
            main_board[clicked] = button["text"]
            if checkForWin(turn):
                print("O WINS")
                game_end = True
            elif checkfordraw():
                print("DRAW")
                game_end = True
            else:
                turn = 'X'

button1 = Button(fram1, text="", width=4, height= 2, font= ("Arial" , 35), bg="black",fg= "white")
button1.grid(row= 0, column= 0)
button1.bind("<Button-1>", play)


button2 = Button(fram1, text="", width=4, height= 2, font= ("Arial" , 35), bg="black",fg= "white")
button2.grid(row= 0, column= 1)
button2.bind("<Button-1>", play)

button3 = Button(fram1, text="", width=4, height= 2, font= ("Arial" , 35), bg="black",fg= "white")
button3.grid(row= 0, column= 2)
button3.bind("<Button-1>", play)

button4 = Button(fram1, text="", width=4, height= 2, font= ("Arial" , 35), bg="black",fg= "white")
button4.grid(row= 1, column= 0)
button4.bind("<Button-1>", play)

button5 = Button(fram1, text="", width=4, height= 2, font= ("Arial" , 35), bg="black",fg= "white")
button5.grid(row= 1, column= 1)
button5.bind("<Button-1>", play)

button6 = Button(fram1, text="", width=4, height= 2, font= ("Arial" , 35), bg="black",fg= "white")
button6.grid(row= 1, column= 2)
button6.bind("<Button-1>", play)

button7 = Button(fram1, text="", width=4, height= 2, font= ("Arial" , 35), bg="black",fg= "white")
button7.grid(row= 2, column= 0)
button7.bind("<Button-1>", play)

button8 = Button(fram1, text="", width=4, height= 2, font= ("Arial" , 35), bg="black",fg= "white")
button8.grid(row= 2, column= 1)
button8.bind("<Button-1>", play)

button9 = Button(fram1, text="", width=4, height= 2, font= ("Arial" , 35), bg="black",fg= "white")
button9.grid(row= 2, column= 2)
button9.bind("<Button-1>", play)



restart = Button(fram1,text= "RESTART",width= 12 , height= 1, font= ("arial", 30), bg= "green" ,command= restart_game)
restart.grid(row=4, column=0, columnspan=3)

all_buttons = [button1,button2,button3,button4,button5,button6,button7,button8,button9]

root.mainloop()

for key,val in main_board.items():
    print(*(key,val))

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

lis = check_empty(main_board)
print(lis)










