import random

# You need to complete this function which should return moves and choice 
# You can use the helper functions provided in the AlgoBot.py file
def group2(self, board):
    possible_moves = self.getPossibleMoves(board)

    # If no valid moves are found, end the turn
    if not possible_moves:
        self.game.end_turn()
        return None, None
    
    # Generate a random valid move
    random_move = random.choice(possible_moves)  # random_move is a tuple: (i, j, valid_moves)
    
    # Get the list of valid destinations for the selected piece
    valid_moves_for_piece = random_move[2]  # This should be a list of valid moves (i.e., possible destinations)
    
    # If there are no valid moves for the selected piece, end the turn
    if not valid_moves_for_piece:
        self.game.end_turn()
        return None, None
    
    # Select a random valid destination for the chosen piece
    random_choice = random.choice(valid_moves_for_piece)
    
    # Return the move (current position) and the randomly chosen destination
    return random_move, random_choice
