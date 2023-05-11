import random
import copy

file = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rank = ['8', '7', '6', '5', '4', '3', '2', '1']

class Chess:
    
    def __init__(self):
        self.board = [[' ' for file in range(8)] for rank in range(8)]
        self.player1 = None
        self.player2 = None

        # For simplicity
        self.num_of_rank = 8
        self.num_of_file = 8

    def get_board(self):
        for rank in self.board:
            rank_blocks = []
            for block in rank:
                if len(block) == 2:
                    rank_blocks.append(block[0])
                else:
                    rank_blocks.append(block)
            print(rank_blocks)

    def setup_board(self):
        # P: Pawn, B: Bishop, N: Knight, R: Rook, Q: Queen, K: King
        
        # Initialize Black pieces.
        self.board[0][0] = self.board[0][-1] = ['R', 'Black']
        self.board[0][1] = self.board[0][-2] = ['N', 'Black']
        self.board[0][2] = self.board[0][-3] = ['B', 'Black']
        self.board[0][3] = ['Q', 'Black']
        self.board[0][4] = ['K', 'Black']

        self.board[-1][0] = self.board[-1][-1] = ['R', 'White']
        self.board[-1][1] = self.board[-1][-2] = ['N', 'White']
        self.board[-1][2] = self.board[-1][-3] = ['B', 'White']
        self.board[-1][3] = ['Q', 'White']
        self.board[-1][4] = ['K', 'White']


        # Initialize second rank of each side
        for block in range(self.num_of_file):
            self.board[1][block] = ['P', 'Black']
            self.board[-2][block] = ['P', 'White']

    def select_player(self):
        color = ['White', 'Black']
        (self.player1.player_color, self.player2.player_color) = random.sample(color, 2)
        print(f'{self.player1.player} has {self.player1.player_color} piece and {self.player2.player} has {self.player2.player_color} piece')

        if self.player1.player_color == 'White':
            self.player1.turn = True
            return (f'{self.player1.player} goes first')
        else:
            self.player2.turn = True
            return (f'{self.player2.player} goes first')


class Player1():
    def __init__(self, game, player, turn=False):
        self.game = game
        self.player = player
        self.player_color = ''
        self.turn = turn
        self.point = 0
    
    def update_player(self):
        self.game.player1 = self

    def get_color(self):
        self.player_color = self.game.player1_color
        if self.player_color == 'White':
            self.turn = True

    
    def possible_moves_for_pawn(self, position):
        curr_let = [loc for loc in position]
        # In the game of chess, the order of block naming is file-rank,
        # but in two dimensional arrays, we go through rows first (rank) and then column (file)
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if self.game.board[curr_index[0]][curr_index[1]] == ['P', self.player_color]:
            print(f'{self.player}:  A map of your possible moves for pawn at position {position}:')

            move_set_list = Pawn_possible_moves(self.game, curr_index, self.player_color)
            
            # Visualize possible moves
            move_map = copy.deepcopy(self.game)
            for move in move_set_list:
                if self.game.board[move[0]][move[1]] == ' ':
                    move_map.board[move[0]][move[1]] = '*'
                elif self.game.board[move[0]][move[1]][1] != self.player_color:
                    move_map.board[move[0]][move[1]] = '@'
            return move_map.get_board()


    def possible_moves_for_rook(self, position):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if self.game.board[curr_index[0]][curr_index[1]] == ['R', self.player_color]:
            print(f'{self.player}:  A map of your possible moves for rook at position {position}:')
            move_set_list =  Rook_possible_moves(self.game, curr_index, self.player_color)

            move_map = copy.deepcopy(self.game)
            for move in move_set_list: 
                if self.game.board[move[0]][move[1]] == ' ':
                    move_map.board[move[0]][move[1]] = '*'
                elif self.game.board[move[0]][move[1]][1] != self.player_color:
                    move_map.board[move[0]][move[1]] = '@'
                
            return move_map.get_board()


    def possible_moves_for_knight(self, position):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if self.game.board[curr_index[0]][curr_index[1]] == ['N', self.player_color]:
            print(f'{self.player}:  A map of your possible moves for knight at position {position}:')
            move_set_list = Knight_possible_moves(self.game, curr_index)

            move_map = copy.deepcopy(self.game)
            for move in move_set_list:
                move_map.board[move[0]][move[1]] = '*'
            return move_map.get_board()

    
    def possible_moves_for_bishop(self, position):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if self.game.board[curr_index[0]][curr_index[1]] == ['B', self.player_color]:
            print(f'{self.player}:  A map of your possible moves for bishop at position {position}:')

            move_set_list = Bishop_possible_moves(self.game, curr_index)

            # Visualize possible moves
            move_map = copy.deepcopy(self.game)
            for move in move_set_list:
                move_map.board[move[0]][move[1]] = '*'
            return move_map.get_board()


    def possible_moves_for_queen(self, position):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if self.game.board[curr_index[0]][curr_index[1]] == ['Q', self.player_color]:
            print(f'{self.player}:  A map of your possible moves for queen at position {position}:')
            move_set_list = Queen_possible_moves(self.game, curr_index)

            move_map = copy.deepcopy(self.game)
            for move in move_set_list:
                move_map.board[move[0]][move[1]] = '*'
            return move_map.get_board()

    
    def possible_moves_for_king(self, position):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if self.game.board[curr_index[0]][curr_index[1]] == ['K', self.player_color]:
            print(f'{self.player}:  A map of your possible moves for king at position {position}:')
            move_set_list =  King_possible_moves(self.game, curr_index)

            move_map = copy.deepcopy(self.game)
            for move in move_set_list:
                move_map.board[move[0]][move[1]] = '*'
            return move_map.get_board()


    def move_pawn(self, position_from, position_to):
        if self.turn == False:
            print(f"{self.player}:  Wait for the other player to finishe their turn")
            return

        curr_let = [loc for loc in position_from]
        next_let = [loc for loc in position_to]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        next_index = [rank.index(next_let[1]), file.index(next_let[0])]
        if self.game.board[curr_index[0]][curr_index[1]] == ['P', self.player_color]:
            move_set_list = Pawn_possible_moves(self.game, curr_index, self.player_color)
        else:
            print(f"{self.player}:  Warning: Wrong Piece")
            return False


        if next_index in move_set_list:
            if self.game.board[next_index[0]][next_index[1]][0] == 'P':
                self.point += 1
                print(f'{self.player}:  You have captured the opponent\'s pawn, you earned 1 point')
            elif self.game.board[next_index[0]][next_index[1]][0] == 'N':
                self.point += 3
                print(f'{self.player}:  You have captured the opponent\'s knight, you earned 3 points')
            elif self.game.board[next_index[0]][next_index[1]][0] == 'B':
                self.point += 3
                print(f'{self.player}:  You have captured the opponent\'s bishiop, you earned 3 points')
            elif self.game.board[next_index[0]][next_index[1]][0] == 'R':
                self.point += 5
                print(f'{self.player}:  You have captured the opponent\'s rook, you earned 5 points')
            elif self.game.board[next_index[0]][next_index[1]][0] == 'Q':
                self.point += 9
                print(f'{self.player}:  You have captured the opponent\s queen, you earned 9 points')
            elif self.game.board[next_index[0]][next_index[1]][0] == 'K':
                # Reset the game or update the game so that it cannot be played anymore 
                print(f'{self.player}: You have captured the oppoent\'s king, you won the match')
                return True
            move_piece(self.game, curr_index, next_index)
            print(f'{self.player}:  Pawn at {position_from} has been moved to {position_to}')
            self.turn = False
            self.game.player2.turn = True

        return True

    def move_rook(self, position_from, position_to):
        if self.turn == False:
            print(f"{self.player}:  Wait for the other player to finish their turn")
            return

        curr_let = [loc for loc in position_from]
        next_let = [loc for loc in position_to]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        next_index = [rank.index(next_let[1]), file.index(next_let[0])]
        if self.game.board[curr_index[0]][curr_index[1]] == ['R', self.player_color]:
            move_set_list = Rook_possible_moves(self.game, curr_index, self.player_color)
        else:
            print(f"{self.player}:  Warning: Wrong Piece")
            return False

        if next_index in move_set_list:
            prev = self.game.board[next_index[0]][next_index[1]][0]
            move_piece(self.game, curr_index, next_index)
            print(point_system(self, prev))
            self.turn = False
            self.game.player2.turn = True

        return True

    
    def move_knight(self, position_from, position_to):
        if self.turn == False:
            print(f"{self.player}:  wait for the other player to finish their turn")
            return

        curr_let = [loc for loc in position_from]
        next_let = [loc for loc in position_to]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        next_index = [rank.index(next_let[1]), file.index(next_let[0])]
        if self.game.board[curr_index[0]][curr_index[1]] == ['N', self.player_color]:
            move_set_list = Knight_possible_moves(self.game, curr_index)
        else:
            print(f"{self.player}:  Warning: Wrong Piece")
            return False

        if next_index in move_set_list:
            move_piece(self.game, curr_index, next_index)
            print(f'{self.player}:  Knight at {position_from} has been moved to {position_to}')
            self.turn = False
            self.game.player2.turn = True

            return True
        return False


    def move_bishop(self, position_from, position_to):
        if self.turn == False:
            print(f"{self.player}:  wait for the other player to finish their turn")
            return

        curr_let = [loc for loc in position_from]
        next_let = [loc for loc in position_to]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        next_index = [rank.index(next_let[1]), file.index(next_let[0])]
        if self.game.board[curr_index[0]][curr_index[1]] == ['B', self.player_color]:
            move_set_list = Bishop_possible_moves(self.game, curr_index)
        else:
            print(f"{self.player}:  Warning: Wrong Piece")
            return False

        if next_index in move_set_list:
            move_piece(self.game, curr_index, next_index)
            print(f'{self.player}:  Bishop at {position_from} has been moved to {position_to}')
            self.turn = False
            self.game.player2.turn = True

            return True
        return False


    def move_queen(self, position_from, position_to):
        if self.turn == False:
            print(f"{self.player}:  wait for the other player to finish their turn")
            return

        curr_let = [loc for loc in position_from]
        next_let = [loc for loc in position_to]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        next_index = [rank.index(next_let[1]), file.index(next_let[0])]
        if self.game.board[curr_index[0]][curr_index[1]] == ['Q', self.player_color]:
            move_set_list = Queen_possible_moves(self.game, curr_index)
        else:
            print(f"{self.player}:  Warning: Wrong Piece")
            return False

        if next_index in move_set_list:
            move_piece(self.game, curr_index, next_index)
            print(f'{self.player}:  Queen at {position_from} has been moved to {position_to}')
            self.turn = False
            self.game.player2.turn = True

            return True
        return False


    def move_king(self, position_from, position_to):
        if self.turn == False:
            print(f"{self.player}:  wait for the other player to finish their turn")
            return

        curr_let = [loc for loc in position_from]
        next_let = [loc for loc in position_to]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        next_index = [rank.index(next_let[1]), file.index(next_let[0])]
        if self.game.board[curr_index[0]][curr_index[1]] == ['K', self.player_color]:
            move_set_list = King_possible_moves(self.game, curr_index)
        else:
            print(f"{self.player}:  Warning: Wrong Piece")
            return False

        if next_index in move_set_list:
            move_piece(self.game, curr_index, next_index)
            print(f'{self.player}:  King at {position_from} has been moved to {position_to}')
            self.turn = False
            self.game.player2.turn = True

            return True
        return False
            

class Player2():
    def __init__(self, game, player, turn=False):
        self.game = game
        self.player = player
        self.player_color = ''
        self.turn = turn
        self.point = 0

    def update_player(self):
        self.game.player2 = self

    def get_color(self):
        self.player_color = self.game.player2_color
        if self.player_color == 'White':
            self.turn = True

    def possible_moves_for_pawn(self, position):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if self.game.board[curr_index[0]][curr_index[1]] == ['P', self.player_color]:
            print(f'{self.player}:  A map of your possible moves for pawn at position {position}:')
            move_set_list = Pawn_possible_moves(self.game, curr_index, self.player_color)
            
            move_map = copy.deepcopy(self.game)
            for move in move_set_list:
                if self.game.board[move[0]][move[1]] == ' ':
                    move_map.board[move[0]][move[1]] = '*'
                elif self.game.board[move[0]][move[1]][1] != self.player_color:
                    move_map.board[move[0]][move[1]] = '@'
            return move_map.get_board()

    
    def possible_moves_for_rook(self, position):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if self.game.board[curr_index[0]][curr_index[1]] == ['R', self.player_color]:
            print(f'{self.player}:  A map of your possible moves for rook at position {position}:')
            move_set_list = Rook_possible_moves(self.game, curr_index, self.player_color)

            move_map = copy.deepcopy(self.game)
            for move in move_set_list:
                if self.game.board[move[0]][move[1]] == ' ':
                    move_map.board[move[0]][move[1]] = '*'
                elif self.game.board[move[0]][move[1]][1] != self.player_color:
                    move_map.board[move[0]][move[1]] = '@'
            return move_map.get_board()


    def possible_moves_for_knight(self, position):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if self.game.board[curr_index[0]][curr_index[1]] == ['N', self.player_color]:
            print(f'{self.player}:  A map of your possible moves for knight at position {position}:')
            move_set_list = Knight_possible_moves(self.game, curr_index)

            move_map = copy.deepcopy(self.game)
            for move in move_set_list:
                move_map.board[move[0]][move[1]] = '*'
            return move_map.get_board()
    

    def possible_moves_for_bishop(self, position):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if self.game.board[curr_index[0]][curr_index[1]] == ['B', self.player_color]:
            print(f'{self.player}:  A map of your possible moves for bishop at position {position}:')
            move_set_list = Bishop_possible_moves(self.game, curr_index)

            move_map = copy.deepcopy(self.game)
            for move in move_set_list:
                move_map.board[move[0]][move[1]] = '*'
            return move_map.get_board()


    def possible_moves_for_queen(self, position):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if self.game.board[curr_index[0]][curr_index[1]] == ['Q', self.player_color]:
            print(f'{self.player}:  A map of your possible moves for queen at position {position}:')
            move_set_list = Queen_possible_moves(self.game, curr_index)

            move_map = copy.deepcopy(self.game)
            for move in move_set_list:
                move_map.board[move[0]][move[1]] = '*'
            return move_map.get_board()


    def possible_moves_for_king(self, position):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if self.game.board[curr_index[0]][curr_index[1]] == ['K', self.player_color]:
            print(f'{self.player}:  A map of your possible moves for king at position {position}:')
            move_set_list = King_possible_moves(self.game, curr_index)

            move_map = copy.deepcopy(self.game)
            for move in move_set_list:
                move_map.board[move[0]][move[1]] = '*'
            return move_map.get_board()


    def move_pawn(self, position_from, position_to):
        if self.turn == False:
            print(f"{self.player}:  Wait for the other player to finish their turn.")
            return
        
        curr_let = [loc for loc in position_from]
        next_let = [loc for loc in position_to]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        next_index = [rank.index(next_let[1]), file.index(next_let[0])]
        if self.game.board[curr_index[0]][curr_index[1]] == ['P', self.player_color]:
            move_set_list = Pawn_possible_moves(self.game, curr_index, self.player_color)
        else:
            print(f"{self.player}:  Warning: Wrong Piece")
            return False

        if next_index in move_set_list:
            if self.game.board[next_index[0]][next_index[1]][0] == 'P':
                self.point += 1
                print(f'{self.player}:  You have captured the opponent\'s pawn, you earned 1 point')
            elif self.game.board[next_index[0]][next_index[1]][0] == 'N':
                self.point += 3
                print(f'{self.player}:  You have captured the opponent\'s knight, you earned 3 points')
            elif self.game.board[next_index[0]][next_index[1]][0] == 'B':
                self.point += 3
                print(f'{self.player}:  You have captured the opponent\'s bishiop, you earned 3 points')
            elif self.game.board[next_index[0]][next_index[1]][0] == 'R':
                self.point += 5
                print(f'{self.player}:  You have captured the opponent\'s rook, you earned 5 points')
            elif self.game.board[next_index[0]][next_index[1]][0] == 'Q':
                self.point += 9
                print(f'{self.player}:  You have captured the opponent\s queen, you earned 9 points')
            elif self.game.board[next_index[0]][next_index[1]][0] == 'K':
                # Reset the game or update the game so that it cannot be played anymore 
                print(f'{self.player}: You have captured the oppoent\'s king, you won the match')
                return True
            move_piece(self.game, curr_index, next_index)
            print(f'{self.player}:  Pawn at {position_from} has been moved to {position_to}')
            self.turn = False
            self.game.player1.turn = True

        return True

    
    def move_rook(self, position_from, position_to):
        if self.turn == False:
            print(f"{self.player}:  Wait for the other player to finish their turn.")
            return

        curr_let = [loc for loc in position_from]
        next_let = [loc for loc in position_to]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        next_index = [rank.index(next_let[1]), file.index(next_let[0])]
        if self.game.board[curr_index[0]][curr_index[1]] == ['R', self.player_color]:
            move_set_list = Rook_possible_moves(self.game, curr_index, self.player_color)
        else:
            print(f"{self.player}:  Warning: Wrong Piece")
            return False

        if next_index in move_set_list:
            prev = self.game.board[next_index[0]][next_index[1]][0]
            move_piece(self.game, curr_index, next_index)
            print(f'{self.player}:  Rook at {position_from} has been moved to {position_to}')
            print(point_system(self, prev)) 
            self.turn = False
            self.game.player1.turn = True

        return True

    
    def move_knight(self, position_from, position_to):
        if self.turn == False:
            print(f"{self.player}:  wait for the other player to finish their turn")
            return False

        curr_let = [loc for loc in position_from]
        next_let = [loc for loc in position_to]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        next_index = [rank.index(next_let[1]), file.index(next_let[0])]
        if self.game.board[curr_index[0]][curr_index[1]] == ['N', self.player_color]:
            move_set_list = Knight_possible_moves(self.game, curr_index)
        else:
            print(f"{self.player}:  Warning: Wrong Piece")
            return False

        if next_index in move_set_list:
            move_piece(self.game, curr_index, next_index)
            print(f'{self.player}:  Knight at {position_from} has been moved to {position_to}')
            self.turn = False
            self.game.player1.turn = True

        return True


    def move_bishop(self, position_from, position_to):
        if self.turn == False:
            print(f"{self.player}:  wait for the other player to finish their turn")
            return

        curr_let = [loc for loc in position_from]
        next_let = [loc for loc in position_to]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        next_index = [rank.index(next_let[1]), file.index(next_let[0])]
        if self.game.board[curr_index[0]][curr_index[1]] == ['B', self.player_color]:
            move_set_list = Bishop_possible_moves(self.game, curr_index)
        else:
            print(f"{self.player}:  Warning: Wrong Piece")
            return False

        if next_index in move_set_list:
            move_piece(self.game, curr_index, next_index)
            print(f'{self.player}:  Bishop at {position_from} has been moved to {position_to}')
            self.turn = False
            self.game.player1.turn = True

            return True
        return False


    def move_queen(self, position_from, position_to):
        if self.turn == False:
            print(f"{self.player}:  wait for the other player to finish their turn")
            return

        curr_let = [loc for loc in position_from]
        next_let = [loc for loc in position_to]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        next_index = [rank.index(next_let[1]), file.index(next_let[0])]
        if self.game.board[curr_index[0]][curr_index[1]] == ['Q', self.player_color]:
            move_set_list = Queen_possible_moves(self.game, curr_index)
        else:
            print(f"{self.player}:  Warning: Wrong Piece")
            return False

        if next_index in move_set_list:
            move_piece(self.game, curr_index, next_index)
            print(f'{self.player}:  Queen at {position_from} has been moved to {position_to}')
            self.turn = False
            self.game.player2.turn = True

            return True
        return False


    def move_king(self, position_from, position_to):
        if self.turn == False:
            print(f"{self.player}:  wait for the other player to finish their turn")
            return

        curr_let = [loc for loc in position_from]
        next_let = [loc for loc in position_to]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        next_index = [rank.index(next_let[1]), file.index(next_let[0])]
        if self.game.board[curr_index[0]][curr_index[1]] == ['K', self.player_color]:
            move_set_list = King_possible_moves(self.game, curr_index)
        else:
            print(f"{self.player}:  Warning: Wrong Piece")
            return False

        if next_index in move_set_list:
            move_piece(self.game, curr_index, next_index)
            print(f'{self.player}:  King at {position_from} has been moved to {position_to}')
            self.turn = False
            self.game.player2.turn = True

            return True
        return False


def Rook_possible_moves(game, index, color):
    move_set_list = []

    ptr = index
    while ptr[0] > 0:
        ptr = [ptr[0] - 1, ptr[1]]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)
        else:
            if game.board[ptr[0]][ptr[1]][1] != color:
                move_set_list.append(ptr)
            break

    ptr = index
    while ptr[0] < len(rank) - 1:
        ptr = [ptr[0] + 1, ptr[1]]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)
        else:
            if game.board[ptr[0]][ptr[1]][1] != color:
                move_set_list.append(ptr)
            break

    ptr = index
    while ptr[1] > 0:
        ptr = [ptr[0], ptr[1] - 1]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)
        else:
            if game.board[ptr[0]][ptr[1]][1] != color:
                move_set_list.append(ptr)
            break
    
    ptr = index
    while ptr[1] < len(file) - 1:
        ptr = [ptr[0], ptr[1] + 1]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)
        else:
            if game.board[ptr[0]][ptr[1]][1] != color:
                move_set_list.append(ptr)
            break

    return move_set_list


def Knight_possible_moves(game, index):
    move_set_list = []

    # one-up two-left
    ptr = index
    if ptr[0] -1 >= 0 and ptr[1] - 2 > 0:
        ptr = [ptr[0] - 1, ptr[1] - 2]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)
    
    # two-up one-left
    ptr = index
    if ptr[0] - 2 >= 0 and ptr[1] - 1 >= 0:
        ptr = [ptr[0] - 2, ptr[1] - 1]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)

    # one-up two-right
    ptr = index
    if ptr[0] - 1 >= 0 and ptr[1] + 2 < len(file):
        ptr = [ptr[0] - 1, ptr[1] + 2]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)

    # two-up one-right
    ptr = index
    if ptr[0] - 2 >= 0 and ptr[1] + 1 < len(file):
        ptr = [ptr[0] - 2, ptr[1] + 1]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)

    # one-down two-left
    ptr = index
    if ptr[0] + 1 < len(rank) and ptr[1] - 2 >= 0:
        ptr = [ptr[0] + 1, ptr[1] -2]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)

    # two-down one-left
    ptr = index
    if ptr[0] + 2 < len(rank) and ptr[1] - 1 >= 0:
        ptr = [ptr[0] + 2, ptr[1] - 1]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)

    # one-down two-right
    ptr = index
    if ptr[0] + 1 < len(rank) and ptr[1] + 2 < len(file):
        ptr = [ptr[0] + 1, ptr[1] + 2]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)

    # two-down one-right
    ptr = index
    if ptr[0] + 2 < len(rank) and ptr[1] + 1 < len(file):
        ptr = [ptr[0] + 2, ptr[1] + 1]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)

    return move_set_list


def Bishop_possible_moves(game, index):
    move_set_list = []

    # Case 1: Up-left
    ptr = index
    while ptr[0] > 0 and ptr[1] > 0:
        ptr = [ptr[0] - 1, ptr[1] - 1]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)
        else:
            break

    # Case 2: up-right
    ptr = index
    while ptr[0] > 0 and ptr[1] < len(file) - 1:
        ptr = [ptr[0] - 1, ptr[1] + 1]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)
        else:
            break

    # Case 3: down-left
    ptr = index
    while ptr[0] < len(rank) - 1 and ptr[1] > 0:
        ptr = [ptr[0] + 1, ptr[1] - 1]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)
        else:
            break

    # Case 4: down-right
    ptr = index
    while ptr[0] < len(rank) - 1 and ptr[1] < len(file) - 1:
        ptr = [ptr[0] + 1, ptr[1] + 1]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)
        else:
            break
    
    return move_set_list


def Queen_possible_moves(game, index):
    move_set_list_cross = Rook_possible_moves(game, index)
    move_set_list_diagonal = Bishop_possible_moves(game, index)
    move_set_list = move_set_list_cross + move_set_list_diagonal

    return move_set_list

def King_possible_moves(game, index):
    move_set_list = []

    ptr = index
    # surrounding three ranks of current index
    for rank_i in range(ptr[0] - 1, ptr[0] + 2):
        # surrounding three files of current index
        for file_i in range(ptr[1] - 1, ptr[1] + 2):
            # check if new  index is within the range of the board and if new index is not equalt to previous index.
            if rank_i >= 0 and file_i >= 0 and rank_i <= len(rank) - 1 and file_i <= len(file) - 1 and [rank_i, file_i] != index:
                # if it is within the range and not equal to previous index, check if block at this index is already filled in.
                if game.board[rank_i][file_i] == ' ':
                    move_set_list.append([rank_i, file_i])

    return move_set_list

def Pawn_possible_moves(game, index, color):
    move_set_list = []
    
    ptr = index
    # White pawn's moves
    if color == "White" and ptr[0] > 0:
        # top two diagonal blocks of current index
        for file_i in range(ptr[1] - 1, ptr[1] + 2, 2):
            if file_i >= 0 and file_i < len(file):
                if game.board[ptr[0] - 1][file_i] == ' ' or game.board[ptr[0] - 1][file_i][1] != color:
                    move_set_list.append([ptr[0] - 1, file_i])

    # Black pawn's moves
    if color == "Black" and ptr[0] < len(rank):
        # bottom two diagonal blocks of current index
        for file_i in range(ptr[1] - 1, ptr[1] + 2, 2):
            if file_i >= 0 and file_i < len(file):
                if game.board[ptr[0] + 1][file_i] == ' ' or game.board[ptr[0] + 1][file_i][1] != color:
                    move_set_list.append([ptr[0] + 1, file_i])

    return move_set_list


def move_piece(game, index_from, index_to):
    temp = game.board[index_from[0]][index_from[1]]
    game.board[index_from[0]][index_from[1]] = ' '
    game.board[index_to[0]][index_to[1]] = temp


def point_system(player, target):
    if target == 'P':
        player.point += 1
        return(f'{player.player}:  You have captured the opponent\'s pawn, you earned 1 point')
    elif target == 'N':
        player.point += 3
        return(f'{player.player}:  You have captured the opponent\'s knight, you earned 3 points')
    elif target == 'B':
        player.point += 3
        return(f'{player.player}:  You have captured the opponent\'s bishiop, you earned 3 points')
    elif target == 'R':
        player.point += 5
        return(f'{player.player}:  You have captured the opponent\'s rook, you earned 5 points')
    elif target == 'Q':
        player.point += 9
        return(f'{player.player}:  You have captured the opponent\s queen, you earned 9 points')
    elif target == 'K':
        # Reset the game or update the game so that it cannot be played anymore 
        return(f'{player.player}: You have captured the oppoent\'s king, you won the match')