#Assumed that user does not enter into the same location again
#No Graphics (beautification)
#turn=input("Whose turn X or O:")
board = ['--','--','--',
         '--','--','--',
         '--','--','--']
used = []
noofturns=0
def print_board():
    for i in range (9):
      print(board[i],end='\t')
      if ((i+1)%3==0):
          print()
def take_turn(turn):
  if turn == 'X':
      print("X\'s Turn")
      temp=int(input('Enter your choice:'))
      board[temp]='X'
      turn='O'
  else:
      print("O\'s Turn")
      temp=int(input('Enter your choice:'))
      board[temp]='O'
      turn='X'


#print_board()
#take_turn(turn)
#print_board()


































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


