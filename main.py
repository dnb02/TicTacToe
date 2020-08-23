
#Assumed that user does not enter into the same location again
#No Graphics (beautification)
noofturns=0
win='n'
turn=input("Whose turn X or O:")
board = ['--','--','--',
         '--','--','--',
         '--','--','--']
def print_board():
    for i in range (9):
      print(board[i],end='\t')
      if ((i+1)%3==0):
          print()
def take_turn(t,no):
  global turn
  global noofturns
  if t == 'X':
      print("X\'s Turn")
      temp=int(input('Enter your choice:'))
      board[temp]='X'
      turn='O'
  else:
      print("O\'s Turn")
      temp=int(input('Enter your choice:'))
      board[temp]='O'
      turn='X'
  noofturns=no+1
def check_win():
  global win
  win='n'
  if(board[0]==board[1] and board[1]==board[2]):
    win=board[0]
  elif (board[3]==board[4] and board[4]==board[5]):
    win=board[3]
  elif (board[6]==board[7] and board[7]==board[8]):
    win=board[6]  
  elif (board[3]==board[4] and board[4]==board[5]):
    win=board[3]
  elif (board[0]==board[3] and board[3]==board[6]):
    win=board[3]
  elif (board[1]==board[4] and board[4]==board[7]):
    win=board[1]
  elif (board[2]==board[5] and board[5]==board[8]):
    win=board[2]
  elif (board[0]==board[4] and board[4]==board[8]):
    win=board[0]
  elif (board[2]==board[4] and board[4]==board[6]):
    win=board[4]
  else:
    print(' ')
  if win != 'n' :
    print('The Winner is ',win)
    exit()
print_board()
for i in range (9): 
 take_turn(turn,noofturns)
 print_board()
 if (i > 3):
   check_win()



































#def check(val,noofturns):
# if noofturns == 0:
#  used.append(val)
# else:
#   for i in range(noofturns):
#    print (i)
#    if(used[i]==val):
#      print("Sorry that choice is taken\nEnter any other number")
#      break
#    break
#    if(i+1==noofturns):
#      used.append(val)


