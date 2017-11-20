#!/usr/bin/python
import random

def pb():
	print (str(''.join(board [0])) + '\n' + str(''.join(board [1])) + '\n' + str(''.join(board [2])) + '\n' + str(''.join(board [3])) + '\n' + str(''.join(board [4])) + '\n')
	
def checkVictory():
	#Check for player victory
	
	#Check rows for player victory
	if ((board [0] [0] == 'X|') and (board [0] [1] == 'X|') and (board [0] [2] == 'X')):
		pb()
		print('YOU WIN!!!\n')
		return False
	elif((board [2] [0] == 'X|') and (board [2] [1] == 'X|') and (board [2] [2] == 'X')):
		pb()
		print('YOU WIN!!!\n')
		return False
	elif ((board [4] [0] == 'X|') and (board [4] [1] == 'X|') and (board [4] [2] == 'X')):
		pb()
		print('YOU WIN!!!\n')
		return False
	
	#Check Colum for player victory
	elif ((board [0] [0] == 'X|') and (board [2] [0] == 'X|') and (board [4] [0] == 'X|')):
		pb()
		print('YOU WIN!!!\n')
		return False
	elif ((board [0] [1] == 'X|') and (board [2] [1] == 'X|') and (board [4] [1] == 'X|')):
		pb()
		print('YOU WIN!!!\n')
		return False
	elif ((board [0] [2] == 'X') and (board [2] [2] == 'X') and (board [4] [2] == 'X')):
		pb()
		print('YOU WIN!!!\n')
		return False
	
	#Check diags for player victory	
	elif ((board [0] [0] == 'X|') and (board [2] [1] == 'X|') and (board [4] [2] == 'X')):
		pb()
		print('YOU WIN!!!\n')
		return False
	elif ((board [0] [2] == 'X') and (board [2] [1] == 'X|') and (board [4] [0] == 'X|')):
		pb()
		print('YOU WIN!!!\n')
		return False
		
	#Check for computer victory
	
	#Check rows for computer victory
	elif ((board [0] [0] == 'O|') and (board [0] [1] == 'O|') and (board [0] [2] == 'O')):
		pb()
		print('YOU LOSE!!!\n')
		return False
	elif((board [2] [0] == 'O|') and (board [2] [1] == 'O|') and (board [2] [2] == 'O')):
		pb()
		print('YOU LOSE!!!\n')
		return False
	elif ((board [4] [0] == 'O|') and (board [4] [1] == 'O|') and (board [4] [2] == 'O')):
		pb()
		print('YOU LOSE!!!\n')
		return False
	
	#Check Colum for computer victory
	elif ((board [0] [0] == 'O|') and (board [2] [0] == 'O|') and (board [4] [0] == 'O|')):
		pb()
		print('YOU LOSE!!!\n')
		return False
	elif ((board [0] [1] == 'O|') and (board [2] [1] == 'O|') and (board [4] [1] == 'O|')):
		pb()
		print('YOU LOSE!!!\n')
		return False
	elif ((board [0] [2] == 'O') and (board [2] [2] == 'O') and (board [4] [2] == 'O')):
		pb()
		print('YOU LOSE!!!\n')
		return False
	
	#Check diags for computer victory	
	elif ((board [0] [0] == 'O|') and (board [2] [1] == 'O|') and (board [4] [2] == 'O')):
		pb()
		print('YOU LOSE!!!\n')
		return False
	elif ((board [0] [2] == 'O') and (board [2] [1] == 'O|') and (board [4] [0] == 'O|')):
		pb()
		print('YOU LOSE!!!\n')
		return False
	
	#Check for Tie
	
	elif ((board [0] [0] != ' |') and (board [0] [1] != ' |') and (board [0] [2] != ' ') and (board [2] [0] != ' |') and (board [2] [1] != ' |') and (board [2] [2] != ' ') and (board [4] [0] != ' |') and (board [4] [1] != ' |') and (board [4] [2] != ' ')):
		pb()
		print('TIE!!!\n')
		return False
	
def player():
	while True:
		userSpot = raw_input('Enter the number spot you wish to take: ')
		print('\n')
		if ((userSpot == '1') and (board [0] [0] == ' |')):
			board [0] [0] = 'X|'
			break
		elif ((userSpot == '2') and (board [0] [1] == ' |')):
			board [0] [1] = 'X|'
			break
		elif ((userSpot == '3') and (board [0] [2] == ' ')):
			board [0] [2] = 'X'
			break
		elif ((userSpot == '4') and (board [2] [0] == ' |')):
			board [2] [0] = 'X|'
			break
		elif ((userSpot == '5') and (board [2] [1] == ' |')):
			board [2] [1] = 'X|'
			break
		elif ((userSpot == '6') and (board [2] [2] == ' ')):
			board [2] [2] = 'X'
			break
		elif ((userSpot == '7') and (board [4] [0] == ' |')):
			board [4] [0] = 'X|'
			break
		elif ((userSpot == '8') and (board [4] [1] == ' |')):
			board [4] [1] = 'X|'
			break
		elif ((userSpot == '9') and (board [4] [2] == ' ')):
			board [4] [2] = 'X'
			break
		else:
			print('That spot is already taken.')
			continue

def computer(first1):
	while True:
		randPrioritSpot = random.randint(1,4)
		randSpot = random.randint(6,10)
		
		#Logic Finish
		
		#Row OO_
		if ((board [0] [0] == 'O|') and (board [0] [1] == 'O|') and (board [0] [2] == ' ')): #top OO_
			board [0] [2] = 'O'
			break
		elif ((board [2] [0] == 'O|') and (board [2] [1] == 'O|') and (board [2] [2] == ' ')): #mid OO_
			board [2] [2] = 'O'
			break
		elif ((board [4] [0] == 'O|') and (board [4] [1] == 'O|') and (board [4] [2] == ' ')): #bottom OO_
			board [4] [2] = 'O'
			break
			
		#Row _OO
		elif ((board [0] [1] == 'O|') and (board [0] [2] == 'O') and (board [0] [0] == ' |')): #top _OO
			board [0] [0] = 'O|'
			break
		elif ((board [2] [1] == 'O|') and (board [2] [2] == 'O') and (board [2] [0] == ' |')): #mid _OO
			board [2] [0] = 'O|'
			break
		elif ((board [4] [1] == 'O|') and (board [4] [2] == 'O') and (board [4] [0] == ' |')): #bottom _OO
			board [4] [0] = 'O|'
			break	
		
		#Colum OO_
		elif ((board [0] [0] == 'O|') and (board [2] [0] == 'O|') and (board [4] [0] == ' |')): #1st colum OO_
			board [4] [0] = 'O|'
			break
		elif ((board [0] [1] == 'O|') and (board [2] [1] == 'O|') and (board [4] [1] == ' |')): #2nd colum OO_
			board [4] [1] = 'O|'
			break
		elif ((board [0] [2] == 'O') and (board [2] [2] == 'O') and (board [4] [2] == ' ')): #3rd colum OO_
			board [4] [2] = 'O'
			break
		
		#Colum _OO
		elif ((board [2] [0] == 'O|') and (board [4] [0] == 'O|') and (board [0] [0] == ' |')): #1st colum _OO
			board [0] [0] = 'O|'
			break
		elif ((board [2] [1] == 'O|') and (board [4] [1] == 'O|') and (board [0] [1] == ' |')): #2nd colum _OO
			board [0] [1] = 'O|'
			break
		elif ((board [2] [2] == 'O') and (board [4] [2] == 'O') and (board [0] [2] == ' ')): #3rd colum _OO
			board [0] [2] = 'O'
			break
	
		#Colum O_O
		elif ((board [0] [0] == 'O|') and (board [4] [0] == 'O|') and (board [2] [0] == ' |')): #1st colum O_O
			board [2] [0] = 'O|'
			break
		elif ((board [0] [1] == 'O|') and (board [4] [1] == 'O|') and (board [2] [1] == ' |')): #2nd colum O_O
			board [2] [1] = 'O|'
			break
		elif ((board [0] [2] == 'O') and (board [4] [2] == 'O') and (board [2] [2] == ' ')): #2nd colum O_O
			board [2] [2] = 'O'
			break
		
		#Row O_O
		elif ((board [0] [0] == 'O|') and (board [0] [2] == 'O') and (board [0] [1] == ' |')): #top O_O
			board [0] [1] = 'O|'
			break
		elif ((board [2] [0] == 'O|') and (board [2] [2] == 'O') and (board [2] [1] == ' |')): #mid O_O
			board [2] [1] = 'O|'
			break
		elif ((board [4] [0] == 'O|') and (board [4] [2] == 'O') and (board [4] [1] == ' |')): #bottom O_O
			board [4] [1] = 'O|'
			break
		
		#Diag L-R
		elif ((board [0] [0] == 'O|') and (board [4] [2] == 'O') and (board [2] [1] == ' |')): #diag L-R O_O
			board [2] [1] = 'O|'
			break
		elif ((board [2] [1] == 'O|') and (board [4] [2] == 'O') and (board [0] [0] == ' |')):#diag L-R _OO
			board [0] [0] = 'O|'
			break
		elif ((board [0] [0] == 'O|') and (board [2] [1] == 'O|') and (board [4] [2] == ' ')): #diag L-R OO_
			board [4] [2] = 'O'
			break
	
		#Diag R-L
		elif ((board [0] [2] == 'O') and (board [4] [0] == 'O|') and (board [2] [1] == ' |')): #diag R-L O_O
			board [2] [1] = 'O|'
			break
		elif ((board [2] [1] == 'O|') and (board [4] [0] == 'O|') and (board [0] [2] == ' ')): #diag R-L _OO
			board [0] [2] = 'O'
			break
		elif ((board [0] [2] == 'O') and (board [2] [1] == 'O|') and (board [4] [0] == ' |')): #diag R-L OO_
			board [4] [0] = 'O|'
			break
		
		#Logic Prevent
		
		#Row XX_
		elif ((board [0] [0] == 'X|') and (board [0] [1] == 'X|') and (board [0] [2] == ' ')): #top XX_
			board [0] [2] = 'O'
			break
		elif ((board [2] [0] == 'X|') and (board [2] [1] == 'X|') and (board [2] [2] == ' ')): #mid XX_
			board [2] [2] = 'O'
			break
		elif ((board [4] [0] == 'X|') and (board [4] [1] == 'X|') and (board [4] [2] == ' ')): #bottom XX_
			board [4] [2] = 'O'
			break
			
		#Row XX_
		elif ((board [0] [1] == 'X|') and (board [0] [2] == 'X') and (board [0] [0] == ' |')): #top _XX
			board [0] [0] = 'O|'
			break
		elif ((board [2] [1] == 'X|') and (board [2] [2] == 'X') and (board [2] [0] == ' |')): #mid _XX
			board [2] [0] = 'O|'
			break
		elif ((board [4] [1] == 'X|') and (board [4] [2] == 'X|') and (board [4] [0] == ' |')): #bottom _XX
			board [4] [0] = 'O|'
			break
	
		#Colum XX_
		elif ((board [0] [0] == 'X|') and (board [2] [0] == 'X|') and (board [4] [0] == ' |')): #1st colum XX_
			board [4] [0] = 'O|'
			break
		elif ((board [0] [1] == 'X|') and (board [2] [1] == 'X|') and (board [4] [1] == ' |')): #2nd colum XX_
			board [4] [1] = 'O|'
			break
		elif ((board [0] [2] == 'X') and (board [2] [2] == 'X') and (board [4] [2] == ' ')): #3rd colum XX_
			board [4] [2] = 'O'
			break
			
		#Colum _XX
		elif ((board [2] [0] == 'X|') and (board [4] [0] == 'X|') and (board [0] [0] == ' |')): #1st colum _XX
			board [0] [0] = 'O|'
			break
		elif ((board [2] [1] == 'X|') and (board [4] [1] == 'X|') and (board [0] [1] == ' |')): #2nd colum _XX
			board [0] [1] = 'O|'
			break
		elif ((board [2] [2] == 'X') and (board [4] [2] == 'X') and (board [0] [2] == ' ')): #3rd colum _XX
			board [0] [2] = 'O'
			break
		
		#Colum X_X
		elif ((board [0] [0] == 'X|') and (board [4] [0] == 'X|') and (board [2] [0] == ' |')): #1st colum X_X
			board [2] [0] = 'O|'
			break
		elif ((board [0] [1] == 'X|') and (board [4] [1] == 'X|') and (board [2] [1] == ' |')): #2nd colum X_X
			board [2] [1] = 'O|'
			break
		elif ((board [0] [2] == 'X') and (board [4] [2] == 'X') and (board [2] [2] == ' ')): #2nd colum X_X
			board [2] [2] = 'O'
			break
		
		#Row X_X
		elif ((board [0] [0] == 'X|') and (board [0] [2] == 'X') and (board [0] [1] == ' |')): #top X_X
			board [0] [1] = 'O|'
			break
		elif ((board [2] [0] == 'X|') and (board [2] [2] == 'X') and (board [2] [1] == ' |')): #mid X_X
			board [2] [1] = 'O|'
			break
		elif ((board [4] [0] == 'X|') and (board [4] [2] == 'X') and (board [4] [1] == ' |')): #bottom X_X
			board [4] [1] = 'O|'
			break
		
		#Diag L-R
		elif ((board [0] [0] == 'X|') and (board [4] [2] == 'X') and (board [2] [1] == ' |')): #diag L-R X_X
			board [2] [1] = 'O|'
			break
		elif ((board [2] [1] == 'X|') and (board [4] [2] == 'X') and (board [0] [0] == ' |')):#diag L-R _XX
			board [0] [0] = 'O|'
			break
		elif ((board [0] [0] == 'X|') and (board [2] [1] == 'X|') and (board [4] [2] == ' ')): #diag L-R XX_
			board [4] [2] = 'O'
			break
	
		#Diag R-L
		elif ((board [0] [2] == 'X') and (board [4] [0] == 'X|') and (board [2] [1] == ' |')): #diag R-L X_X
			board [2] [1] = 'O|'
			break
		elif ((board [2] [1] == 'X|') and (board [4] [0] == 'X|') and (board [0] [2] == ' ')): #diag R-L _XX
			board [0] [2] = 'O'
			break
		elif ((board [0] [2] == 'X') and (board [2] [1] == 'X|') and (board [4] [0] == ' |')): #diag R-L XX_
			board [4] [0] = 'O|'
			break
			
		#Logic Corners
		# top = t, bottom = b, right = r, left = l		
		elif ((board [0] [2] == 'O') and (board [4] [2] == 'O') and (board [4] [0] == ' |') and (((board [4] [1] == ' |') and (board [2] [1] == ' |')) or ((board [0] [1] == ' |') and (board [2] [1] == ' |')) or ((board [4] [1] == ' |') and (board [0] [1] == ' |')))): #corners tr & br take bl
			board [4] [0] = 'O|'
			break
		elif ((board [0] [2] == 'O') and (board [4] [2] == 'O') and (board [0] [0] == ' |') and (((board [0] [1] == ' |') and (board [2] [1] == ' |')) or ((board [2] [1] == ' |') and (board [2] [2] == ' ')) or ((board [0] [1] == ' |') and (board [2] [2] == ' ')))): #corners tr & br take tl
			board [0] [0] = 'O|'
			break
		elif ((board [0] [0] == 'O|') and (board [0] [2] == 'O') and (board [4] [0] == ' |') and (((board [4] [1] == ' |') and (board [2] [1] == ' |')) or ((board [2] [1] == ' |') and (board [2] [0] == ' |')) or ((board [4] [1] == ' |') and (board [2] [0] == ' |')))): #corners tl & tr take bl
			board [4] [0] = 'O|'
			break
		elif ((board [0] [0] == 'O|') and (board [0] [2] == 'O') and (board [4] [2] == ' ') and (((board [0] [1] == ' |') and (board [2] [1] == ' |')) or ((board [2] [1] == ' |') and (board [2] [2] == ' ')) or ((board [0] [1] == ' |') and (board [2] [2] == ' ')))): #corners tl & tr take br
			board [4] [2] = 'O'
			break
		elif ((board [0] [0] == 'O|') and (board [4] [0] == 'O|') and (board [4] [2] == ' ') and (((board [4] [1] == ' |') and (board [2] [1] == ' |')) or ((board [2] [1] == ' |') and (board [2] [0] == ' |')) or ((board [4] [1] == ' |') and (board [2] [0] == ' |')))): #corners tl & bl take br
			board [4] [2] = 'O'
			break
		elif ((board [0] [0] == 'O|') and (board [4] [0] == 'O|') and (board [0] [2] == ' ') and (((board [0] [1] == ' |') and (board [2] [1] == ' |')) or ((board [2] [1] == ' |') and (board [2] [0] == ' |')) or ((board [0] [1] == ' |') and (board [2] [0] == ' |')))): #corners tl & bl take tr
			board [0] [2] = 'O'
			break
		elif ((board [4] [0] == 'O|') and (board [4] [2] == 'O') and (board [0] [0] == ' |') and (((board [4] [1] == ' |') and (board [2] [1] == ' |')) or ((board [2] [1] == ' |') and (board [2] [0] == ' |')) or ((board [4] [1] == ' |') and (board [2] [0] == ' |')))): #corners bl & br take tl
			board [0] [0] = 'O|'
			break
		elif ((board [4] [0] == 'O|') and (board [4] [2] == 'O') and (board [0] [2] == ' ') and (((board [4] [1] == ' |') and (board [2] [1] == ' |')) or ((board [2] [1] == ' |') and (board [2] [2] == ' ')) or ((board [4] [1] == ' |') and (board [2] [2] == ' ')))): #corners bl & br take tr
			board [0] [2] = 'O'
			break
			
		#If player goes first take the mid
			
		elif ((first1 == True) and (board [2] [1] == ' |')):
			board [2] [1] = 'O|'
			break
		
		#If player goes first and comp takes mid and player takes opposite corner
		elif ((first1 == True) and (board [2] [1] == 'O|') and (board [0] [0] == 'X|') and (board [4] [2] == 'X') and (board [4] [1] == ' |')):
			board [4] [1] = 'O|'
			break
		elif ((first1 == True) and (board [2] [1] == 'O|') and (board [0] [2] == 'X') and (board [4] [0] == 'X|') and (board [0] [1] == ' |')):
			board [0] [1] = 'O|'
			break
			
		#If player takes mid when comp goes first then take opposite corner to the one it took
		elif ((first1 == False) and (board [2] [1] == 'X|') and (board [0] [0] == 'O|')):
			board [4] [2] = 'O'
			break
		elif ((first1 == False) and (board [2] [1] == 'X|') and (board [0] [2] == 'O')):
			board [4] [0] = 'O|'
			break
		elif ((first1 == False) and (board [2] [1] == 'X|') and (board [4] [0] == 'O|')):
			board [0] [2] = 'O'
			break
		elif ((first1 == False) and (board [2] [1] == 'X|') and (board [4] [2] == 'O')):
			board [0] [0] = 'O|'
			break
			
		#Random	(only take mid or corners) give priority for comp to take mid/corners
		#Goes through every number incase one number is chosen and the spot is already taken
			
		elif ((randPrioritSpot == 1) and (board [0] [0] == ' |')):
			board [0] [0] = 'O|'
			break
		elif ((randPrioritSpot == 2) and (board [0] [2] == ' ')):
			board [0] [2] = 'O'
			break
		elif ((randPrioritSpot == 3) and (board [4] [0] == ' |')):
			board [4] [0] = 'O|'
			break
		elif ((randPrioritSpot == 4) and (board [4] [2] == ' ')):
			board [4] [2] = 'O'
			break
			
		elif ((randPrioritSpot == 2) and (board [0] [0] == ' |')):
			board [0] [0] = 'O|'
			break
		elif ((randPrioritSpot == 3) and (board [0] [2] == ' ')):
			board [0] [2] = 'O'
			break
		elif ((randPrioritSpot == 4) and (board [4] [0] == ' |')):
			board [4] [0] = 'O|'
			break
		elif ((randPrioritSpot == 1) and (board [4] [2] == ' ')):
			board [4] [2] = 'O'
			break
			
		elif ((randPrioritSpot == 3) and (board [0] [0] == ' |')):
			board [0] [0] = 'O|'
			break
		elif ((randPrioritSpot == 4) and (board [0] [2] == ' ')):
			board [0] [2] = 'O'
			break
		elif ((randPrioritSpot == 1) and (board [4] [0] == ' |')):
			board [4] [0] = 'O|'
			break
		elif ((randPrioritSpot == 2) and (board [4] [2] == ' ')):
			board [4] [2] = 'O'
			break
			
		elif ((randPrioritSpot == 4) and (board [0] [0] == ' |')):
			board [0] [0] = 'O|'
			break
		elif ((randPrioritSpot == 3) and (board [0] [2] == ' ')):
			board [0] [2] = 'O'
			break
		elif ((randPrioritSpot == 2) and (board [4] [0] == ' |')):
			board [4] [0] = 'O|'
			break
		elif ((randPrioritSpot == 1) and (board [4] [2] == ' ')):
			board [4] [2] = 'O'
			break
		#######
		
		#Random (sides) and middle
		elif ((randSpot == 6) and (board [0] [1] == ' |')):
			board [0] [1] = 'O|'
			break
		elif ((randSpot == 7) and (board [2] [0] == ' |')):
			board [2] [0] = 'O|'
			break
		elif ((randSpot == 8) and (board [2] [2] == ' ')):
			board [2] [2] = 'O'
			break
		elif ((randSpot == 9) and (board [4] [1] == ' |')):
			board [4] [1] = 'O|'
			break
		elif ((randSpot == 10) and (board [2] [1] == ' |')):
			board [2] [1] = 'O|'
			break
		else:
			continue

while True:
	board = [['1|', '2|', '3'], ['--', '--', '-'], ['4|', '5|', '6'], ['--', '--', '-'], ['7|', '8|', '9']]
	print('------------\n\nTIC-TAC-TOE:\n')
	pb()
	board = [[' |', ' |', ' '], ['--', '--', '-'], [' |', ' |', ' '], ['--', '--', '-'], [' |', ' |', ' ']]
	turn = random.randint(1,2)
	while True:
		if turn == 1: #Player first
			first1 = True
			player()
			if (checkVictory() == False):
				break
			computer(first1)
			if (checkVictory() == False):
				break
			pb()
			
		elif turn == 2: #Computer first
			first1 = False
			computer(first1)
			if (checkVictory() == False):
				break
			pb()
			player()
			if (checkVictory() == False):
				break
			
