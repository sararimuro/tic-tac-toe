import gamefuncs

print("Welcome to Tic Tac Toe!")
rematch = True
while rematch == True:
	player1, player2 = gamefuncs.player_input()
	order = gamefuncs.choose_first()
	board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
	while True:
		if gamefuncs.full_boardcheck(board) == False:
			gamefuncs.print_board(board)
			spot = gamefuncs.player_choice(board)
			if order == 3:
				board = gamefuncs.place_marker(board, player1, spot)
				if gamefuncs.win_check(board, player1) == True:
					gamefuncs.print_board(board)
					print("Player 1 wins!")
					break
				order = 4
			elif order == 4:
				board = gamefuncs.place_marker(board, player2, spot)
				if gamefuncs.win_check(board, player2) == True:
					gamefuncs.print_board(board)
					print("Player 2 wins!")
					break
				order = 3
		else:
			#the board is full without a winner, thus it's a draw, then asks for a rematch
			gamefuncs.print_board(board)
			print("It's a draw!")
			break
	rematch = gamefuncs.replay()
else:
	pass
