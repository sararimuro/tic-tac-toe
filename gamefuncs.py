def print_board(board_map):
	''' Prints a board for the Tic Tac Toe game with allocated numbers to tiles'''
	print("\n")
	print(f"* **** * **** * **** *\n*      *      *      *\n*  {board_map[1]}   *  {board_map[2]}   *  {board_map[3]}   *\n*      *      *      *\n", end = "")
	print(f"* **** * **** * **** *\n*      *      *      *\n*  {board_map[4]}   *  {board_map[5]}   *  {board_map[6]}   *\n*      *      *      *\n", end = "")
	print(f"* **** * **** * **** *\n*      *      *      *\n*  {board_map[7]}   *  {board_map[8]}   *  {board_map[9]}   *\n*      *      *      *\n", end = "")
	print("* **** * **** * **** *\n")

def player_input():
	'''Takes in an "X" or "O" as player's input'''
	player1 = input("Player 1: please choose 'X' or 'O': ").upper()
	while player1 != 'O' and player1 != 'X':
		player1 = input("Player 1: please choose 'X' or 'O': ").upper()
	if player1 == 'X':
		player2 = 'O'
	else:
		player2 = 'X'
	return (player1, player2)

def place_marker(board, marker, position):
	'''Takes in a pre-defined map of the board, an 'X' or 'O' marker and puts it into a desired poition on the board'''
	board[position] = marker
	return board

def win_check(board, mark):
	'''Takes in a board list and checks whether any marker has a full row'''
	# a = 1
	# for a in range(len(board)-2):
		# case for sequences 123 456 789, doesn't work because counts sequences like 234 or 678 as wins
		# if (board[a] == board[a+1] == board[a+2] == mark):
			# return True
	# all other cases
	return ((board[1] == board[4] == board[7] == mark) or
	(board[1] == board[2] == board[3] == mark) or
	(board[4] == board[5] == board[6] == mark) or
	(board[7] == board[8] == board[9] == mark) or
	(board[2] == board[5] == board[8] == mark) or
	(board[3] == board[6] == board[9] == mark) or
	(board[1] == board[5] == board[9] == mark) or
	(board[3] == board[5] == board[7] == mark))

def choose_first():
	'''Chooses on the base of a random integer which player goes first'''
	import random
	if random.randint(1,2) == 1:
		print("Player 1 will go first!")
		return 3
	else:
		print("Player 2 will go first!")
		return 4

def space_check(board, spot):
	'''Checks whether a space on the board is available and returns a boolean'''
	return board[spot] == ' '

def full_boardcheck(board):
	'''Checks whether the board is full and return a corresponding boolean'''
	return ' ' not in board

def player_choice(board):
	'''Asks the player for their next position, calls a func to check if it's free'''
	'''and returns the position if it's free for later use'''
	spot = 0
	while spot not in range(1, 10) or not space_check(board, spot):
		try:
			spot = int(input("Choose your next position (1-9): "))
		except:
			pass
	return spot

def replay():
	'''Asks the player for rematch, return boolean'''
	again = input("Do you want to play again? Enter yes or no: ")
	while again.lower() != 'yes' and again.lower() != 'no':
		again = input("I didn't quite catch that...\nWould you like to play again? Enter yes or no: ")
	return again.lower() == 'yes'