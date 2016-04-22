# Connect Four by Basti
#
# This is a console based version of the well-known game Connect Four
#
# Author: Sebastian Niedner



#----------------------------------------------------------------------
#
# FUNCTION: makeBoard
# 
# creates an empty break
#
# RETURNS: empty board with columnsXrows
#
def makeBoard(	width=7		#Width of the Board
				,height=6		#Height of the Board
				):
			 
	#create an two-dimensional list [columns][rows] and return it 		 
	return [[0]*height for i in range(width)]
#
#END Of FUNCTION: makeBoard
#
#----------------------------------------------------------------------
	
# FUNCTION: addCoin
#
# adds player coin to board at given column
#
# RETURNS: true if success
#
def addCoin(board			#the play board
			,player			#number of the player, who to add a chip
			,column			#number of the column to add chip
			,height=6		#Height of the Board
			):
	
	
	for row in range(0, height): #find the lowest 0 in the given column and add coin
	
		if board[column][row] == 0: #if value is zero -> unused cell
				
			board[column][row] = player #add chip by setting value to player number
			#print("Player " + str(player) + " added his coin to column " + str(column))
			
			#chip added -> 
			return True
	
	# column is full
	print("Column is full. Can't add coin.")
	return False
#
#END Of FUNCTION: addCoin
#
#----------------------------------------------------------------------



#----------------------------------------------------------------------
#	
# FUNCTION: checkWin
#	
# check if a given player has won
#
#RETURNS: True if player won
#
def checkWin(	board		#the play board
				,width=7	#Width of the Board
				,height=6	#Height of the Board
				,winBy=4	#Number of how many chips are needed to be connected to win
				,player=1	#number of the player, who to add a chip
				):
	
	for col in range(0, width - winBy + 1): #iterate through all columns except the last three
	
		for row in range(0, height): #iterate through all the rows in the column
		
			#print("Col: " + str(col) + " Row: " + str(row) + " Value: " + str(board[col][row]))
			
			if board[col][row] == player: #if it's the players chip, then check if he won from this location
			
				#print("Is player")
				
				#check of up-right direction
				if row < height - winBy + 1:	#macht nur sinn, wenn man nicht in den obersten 3 reihen ist
					#print("NO")
					for x in range(1, winBy): #iterate through the next #winBy chips to the right
						
						if board[col + x][row + x] != player: #if chip is not the players one, then its not a win
							#print("No Win")
							break
						
					else: #Player Won
						print("### Win Player " + str(player) + " by " + str(winBy) + " to up-right at " + str(col) + "/" + str(row))
						return True
						
				#check of right direction
				
				#print("O")
				for x in range(1, winBy): 
					if board[col + x][row] != player:
						#print("No Win")
						break
					
				else: #Player Won
					print("### Win Player " + str(player)  + " by " + str(winBy) + " to the right at " + str(col) + "/" + str(row))
					return True
						
				#check of down-right 
				if row > winBy - 2: #only when high enough #420
					#print("SO")
					for x in range(1, winBy):
						if board[col + x][row - x] != player:
							#print("SO No Win")
							break
						
					else: #Player Won
						print("### Win Player " + str(player) + " by " + str(winBy) + " down-right at " + str(col) + "/" + str(row))
						return True
						
						
				#check of down direction
				if row > winBy - 2: #only when high enough
					for x in range(1, winBy):
						if board[col][row - x] != player:
							#print("S No Win")
							break
						
					else: #Player Won
						print("### Win Player " + str(player) + " by " + str(winBy) + " down at " + str(col) + "/" + str(row))
						return True
	
	return False
#
#END Of FUNCTION: checkWin
#
#----------------------------------------------------------------------

	
	
#----------------------------------------------------------------------
#			
# FUNCTION:printBoard
#	
# prints out board to console
#			
def printBoard(	board		#the play board
				,width=7	#board width
				,height=6	#board height
				):
				
	print() #empty line
	
	outputstring = "     " #fill this strings with all the text of one line
	
	# make heading
	for col in range(0, width):
		outputstring += str(col) + "   "
	
	#print heading
	print(outputstring)
	
	#iterate through rows and print them
	for row in range(height - 1, -1, -1):
	
		#beginning of line
		outputstring = " " + str(row) + " | "
		
		#add values in columns of the row
		for col in range(0, width):
			
			#player 1 on gets an X
			if board[col][row] == 1:
				outputstring += "X"
			
			#player 1 on gets an O
			elif board[col][row] == 2:
				outputstring += "O"
				
			#no Value gets empty character
			else:
				outputstring += " "
			
			# end of line
			outputstring += " | "
		
		#print row
		print(outputstring)
	
	print() #empty line
#
#END Of FUNCTION: printBoard
#
#----------------------------------------------------------------------	


	
#----------------------------------------------------------------------
#			
# FUNCTION:intInput
#	
#prompts user to input a number greater zero and between minValue and maxValue
#
#
#RETURNS: int number
#
def intInput(	prompt="Enter Number: "	#Prompt to been shown to the user
				,minValue=0				#minimum Value
				,maxValue=0				#maximum Value, if 0 then min and max are ignored
				): 
				
	inputValue = 0
	while True: #try until a valid number has been entered
		try:	#int() can throw ValueError which means its not a valid number
		
			#prompt user
			inputValue = int(input(prompt)) 
			
			#its a valid int
			##now check if number is in given scope
			if inputValue >= 0 and (maxValue == 0 or (inputValue <= maxValue and inputValue >= minValue)):
				
				#value is ok, return it
				return inputValue
			else:
				#number not valid
				print("Number entered is not ok. Try again.")
				
		except ValueError: #int(..) failed 
			print("This was not a Number. Try again.")
#
# END OF FUNCTION:intInput				
#
#----------------------------------------------------------------------



#----------------------------------------------------------------------
#			
# FUNCTION: gameloop
#	
# loop of the connect four game
#
#	creates the board
#	prints it	
#
#	prompts player 1 and 2 to enter the column to drop the chip to
#	adds chip
#	and checks for win
#		
def gameloop(width=7, height=6, winBy=4):

	board = makeBoard(width, height) #init board
	printBoard(board, width, height) #print it
	
	actualPlayer = 1 #player 1 starts
	nextPlayer = 2 #player 2 is next
	
	while True: #while while while
		
		while True: #try to add coin, until succesful
			
			if addCoin(board, actualPlayer, intInput(prompt="Player " + str(actualPlayer) + ": Where do you want to drop your chip?: ", maxValue=width-1), height):
				break
		
		#print board
		printBoard(board, width, height)
		
		#check if actualPlayer has won
		if checkWin(board, width, height, winBy, actualPlayer):
		
			print() #empty line
			
			#ask if user wants to play another game
			if input("Play another game (yes/no)? ") == "yes":
			
				#user wants to play another game -> reset board
				print("Starting new game.")
				board = makeBoard(width, height)
				printBoard(board, width, height)
			else:
				#user doesnt want to play another game -> exit
				return
		
		#swap player
		actualPlayer, nextPlayer = nextPlayer, actualPlayer
		
#			
# END OF FUNCTION: gameloop
#	
#---------------------------------------------------------------------

			
#----------------------------------------------------------------------
#
# SETUP	
#

width = 7 #width of the board
height = 6 #height of the board
winBy = 4 #number of connected coins to win the game
	
print()
print("Welcome to Connect Four by Basti")

# start loop
gameloop(width, height, winBy)

#
# END
#
#----------------------------------------------------------------------

