import random
import copy

file = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rank = ['8', '7', '6', '5', '4', '3', '2', '1']

class Chess:
    
    def __init__(self):
        self.board = [[' ' for file in range(8)] for rank in range(8)]
        self.player1 = ''
        self.player1_color = ''
        self.player2 = ''
        self.player2_color = ''

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
        self.board[0][3] = ['K', 'Black']
        self.board[0][4] = ['Q', 'Black']

        self.board[-1][0] = self.board[-1][-1] = ['R', 'White']
        self.board[-1][1] = self.board[-1][-2] = ['N', 'White']
        self.board[-1][2] = self.board[-1][-3] = ['B', 'White']
        self.board[-1][3] = ['K', 'White']
        self.board[-1][4] = ['Q', 'White']


        # Initialize second rank of each side
        for block in range(self.num_of_file):
            self.board[1][block] = ['P', 'Black']
            self.board[-2][block] = ['P', 'White']

    def select_player(self):
        color = ['White', 'Black']
        (self.player1_color, self.player2_color) = random.sample(color, 2)
        print(f'{self.player1} has {self.player1_color} piece and {self.player2} has {self.player2_color} piece')

        if self.player1_color == 'White':
            return (f'{self.player1} goes first')
        else:
            return (f'{self.player2} goes first')


class Player1():
    def __init__(self, player, turn=False):
        self.player = player
        self.player_color = ''
        self.turn = turn
    
    def update_player(self, game):
        game.player1 = self.player

    def get_color(self, game):
        self.player_color = game.player1_color
        if self.player_color == 'White':
            self.turn = True

    
    def possible_moves_for_pawn(self, position, game):
        curr_let = [loc for loc in position]
        # In the game of chess, the order of block naming is file-rank,
        # but in two dimensional arrays, we go through rows first (rank) and then column (file)
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if game.board[curr_index[0]][curr_index[1]] == ['P', 'White']:
            move_set_list = []

            # Checking if the piece the player is looking for is at the top of the board
            if curr_index[0] < len(rank) - 1:

                # Conrer case 1 - far left
                if curr_index[1] == 0:
                    move_set_index = [curr_index[0] - 1, curr_index[1] + 1]
                    if game.board[move_set_index[0]][move_set_index[1]] == ' ':
                        move_set_list.append(move_set_index)

                # Corner case 2 - far right
                elif curr_index[1] == len(file) - 1:
                    move_set_index = [curr_index[0] -1, curr_index[1] - 1]
                    if game.board[move_set_index[0]][move_set_index[1]] == ' ':
                        move_set_list.append(move_set_index)

                # When the piece is not in the edge of the board
                else:
                    move_set_index = [[curr_index[0] - 1, curr_index[1] - 1], [curr_index[0] -1, curr_index[1] + 1]]
                    for move in move_set_index:
                        if game.board[move[0]][move[1]] == ' ':
                            move_set_list.append(move)

                move_let_list = []
                for move in move_set_list:
                    move_let_list.append([file[move[1]], rank[move[0]]])
                move_set_let = [''.join(move) for move in move_let_list]

                if len(move_set_let) == 2:
                    print(f'Your possible moves for pawn at position {position} are {move_set_let[0]} and {move_set_let[1]}')
                else:
                    print(f'Your possible move for pawn at position {position} is {move_set_let[0]}')

                # deepcopy is required so we don't alternate the original game.
                move_map = copy.deepcopy(game)
                for move in move_set_list:
                    move_map.board[move[0]][move[1]] = '*'
                print(f'A map of your possible moves for pawn at position {position}:')
                return move_map.get_board()

            # The pawn at the position given is at the top of the board.
            else:
                return (f"This pawn at position {position} cannot move forward")

        else:
            return ('Invalid input')


    def possible_moves_for_bishop(self, position, game):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if game.board[curr_index[0]][curr_index[1]] == ['B', self.player_color]:
            print(f'A map of your possible moves for bishop at position {position}:')
            return Bishop_possible_moves(game, curr_index)[1]


    def possibe_moves_for_rook(self, position, game):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if game.board[curr_index[0]][curr_index[1]] == ['R', self.player_color]:
            print(f'A map of your possible moves for rook at position {position}:')
            return Rook_possible_moves(game, curr_index)[1]


    def possible_moves_for_knight(self, position, game):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if game.board[curr_index[0]][curr_index[1]] == ['N', self.player_color]:
            print(f'A map of your possible moves for knight at position {position}:')
            return Knight_possible_moves(game, curr_index)

    
    def possible_moves_for_king(self, position, game):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if game.board[curr_index[0]][curr_index[1]] == ['K', self.player_color]:
            print(f'A map of your possible moves for king at position {position}:')
            return King_possible_moves(game, curr_index)[1]



    

class Player2():
    def __init__(self, player, turn=False):
        self.player = player
        self.player_color = ''
        self.turn = turn

    def update_player(self, game):
        game.player2 = self.player

    def get_color(self, game):
        self.player_color = game.player2_color
        if self.player_color == 'White':
            self.turn = True



def Rook_possible_moves(game, index):
    move_set_list = []

    ptr = index
    while ptr[0] > 0:
        ptr = [ptr[0] - 1, ptr[1]]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)

    ptr = index
    while ptr[0] < len(rank) - 1:
        ptr = [ptr[0] + 1, ptr[1]]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)

    ptr = index
    while ptr[1] > 0:
        ptr = [ptr[0], ptr[1] - 1]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)
    
    ptr = index
    while ptr[1] < len(file) - 1:
        ptr = [ptr[0], ptr[1] + 1]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)

    move_map = copy.deepcopy(game)
    for move in move_set_list:
        move_map.board[move[0]][move[1]] = '*'
    return move_set_list, move_map.get_board()

def Knight_possible_moves(game, index):
    move_set_list = []

    # one-up two-left
    ptr = index
    if ptr[0] -1 >= 0 and ptr[1] - 2 > 0:
        ptr = [ptr[0] - 1, ptr[1] - 2]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.appent(ptr)
    
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

    move_map = copy.deepcopy(game)
    for move in move_set_list:
        move_map.board[move[0]][move[1]] = '*'
    return move_map.get_board()

    



def Bishop_possible_moves(game, index):
    move_set_list = []

    # Case 1: Up-left
    ptr = index
    while ptr[0] > 0 and ptr[1] > 0:
        ptr = [ptr[0] - 1, ptr[1] - 1]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)

    # Case 2: up-right
    ptr = index
    while ptr[0] > 0 and ptr[1] < len(file) - 1:
        ptr = [ptr[0] - 1, ptr[1] + 1]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)

    # Case 3: down-left
    ptr = index
    while ptr[0] < len(rank) - 1 and ptr[1] > 0:
        ptr = [ptr[0] + 1, ptr[1] - 1]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)

    # Case 4: down-right
    ptr = index
    while ptr[0] < len(rank) - 1 and ptr[1] < len(file) - 1:
        ptr = [ptr[0] + 1, ptr[1] + 1]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)
    
    # Visualize possible moves
    move_map = copy.deepcopy(game)
    for move in move_set_list:
        move_map.board[move[0]][move[1]] = '*'
    return move_set_list, move_map.get_board()


def King_possible_moves(game, index):
    move_set_list_cross = Rook_possible_moves(game, index)[0]
    move_set_list_diagonal = Bishop_possible_moves(game, index)[0]
    move_set_list = move_set_list_cross + move_set_list_diagonal
    print(move_set_list)

    move_map = copy.deepcopy(game)
    for move in move_set_list:
        move_map.board[move[0]][move[1]] = '*'
    return move_set_list, move_map.get_board()

    