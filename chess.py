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
        if game.board[curr_index[0]][curr_index[1]] == ['P', self.player_color]:
            print(f'A map of your possible moves for pawn at position {position}:')

            move_set_list = Pawn_possible_moves(game, curr_index, self.player_color)

            # Visualize possible moves
            move_map = copy.deepcopy(game)
            for move in move_set_list:
                move_map.board[move[0]][move[1]] = '*'
            return move_map.get_board()


    def possible_moves_for_rook(self, position, game):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if game.board[curr_index[0]][curr_index[1]] == ['R', self.player_color]:
            print(f'A map of your possible moves for rook at position {position}:')
            move_set_list =  Rook_possible_moves(game, curr_index)

            move_map = copy.deepcopy(game)
            for move in move_set_list:
                move_map.board[move[0]][move[1]] = '*'
            return move_map.get_board()


    def possible_moves_for_knight(self, position, game):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if game.board[curr_index[0]][curr_index[1]] == ['N', self.player_color]:
            print(f'A map of your possible moves for knight at position {position}:')
            move_set_list = Knight_possible_moves(game, curr_index)

            move_map = copy.deepcopy(game)
            for move in move_set_list:
                move_map.board[move[0]][move[1]] = '*'
            return move_map.get_board()

    
    def possible_moves_for_bishop(self, position, game):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if game.board[curr_index[0]][curr_index[1]] == ['B', self.player_color]:
            print(f'A map of your possible moves for bishop at position {position}:')

            move_set_list = Bishop_possible_moves(game, curr_index)

            # Visualize possible moves
            move_map = copy.deepcopy(game)
            for move in move_set_list:
                move_map.board[move[0]][move[1]] = '*'
            return move_map.get_board()

    
    def possible_moves_for_king(self, position, game):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if game.board[curr_index[0]][curr_index[1]] == ['K', self.player_color]:
            print(f'A map of your possible moves for king at position {position}:')
            move_set_list =  King_possible_moves(game, curr_index)

            move_map = copy.deepcopy(game)
            for move in move_set_list:
                move_map.board[move[0]][move[1]] = '*'
            return move_map.get_board()


    def possible_moves_for_queen(self, position, game):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if game.board[curr_index[0]][curr_index[1]] == ['Q', self.player_color]:
            print(f'A map of your possible moves for queen at position {position}:')
            move_set_list = Queen_possible_moves(game, curr_index)

            move_map = copy.deepcopy(game)
            for move in move_set_list:
                move_map.board[move[0]][move[1]] = '*'
            return move_map.get_board()


    def move_pawn(self, position_from, position_to, game):
        curr_let = [loc for loc in position_from]
        next_let = [loc for loc in position_to]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        next_index = [rank.index(next_let[1]), file.index(next_let[0])]
        move_set_list = Pawn_possible_moves(game, curr_index, self.player_color)

        if next_index in move_set_list:
            move_piece(game, curr_index, next_index)
            print(f'Pawn at {position_from} has been moved to {position_to}')

        return True
    

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

    def possible_moves_for_pawn(self, position, game):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if game.board[curr_index[0]][curr_index[1]] == ['P', self.player_color]:
            print(f'A map of your possible moves for pawn at position {position}:')
            move_set_list = Pawn_possible_moves(game, curr_index, self.player_color)

            move_map = copy.deepcopy(game)
            for move in move_set_list:
                move_map.board[move[0]][move[1]] = '*'
            return move_map.get_board()

    
    def possible_moves_for_rook(self, position, game):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if game.board[curr_index[0]][curr_index[1]] == ['R', self.player_color]:
            print(f'A map of your possible moves for rook at position {position}:')
            move_set_list = Rook_possible_moves(game, curr_index)

            move_map = copy.deepcopy(game)
            for move in move_set_list:
                move_map.board[move[0]][move[1]] = '*'
            return move_map.get_board()


    def possible_moves_for_knight(self, position, game):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if game.board[curr_index[0]][curr_index[1]] == ['N', self.player_color]:
            print(f'A map of your possible moves for knight at position {position}:')
            move_set_list = Knight_possible_moves(game, curr_index)

            move_map = copy.deepcopy(game)
            for move in move_set_list:
                move_map.board[move[0]][move[1]] = '*'
            return move_map.get_board()
    

    def possible_moves_for_bishop(self, position, game):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if game.board[curr_index[0]][curr_index[1]] == ['B', self.player_color]:
            print(f'A map of your possible moves for bishop at position {position}:')
            move_set_list = Bishop_possible_moves(game, curr_index)

            move_map = copy.deepcopy(game)
            for move in move_set_list:
                move_map.board[move[0]][move[1]] = '*'
            return move_map.get_board()

    def possible_moves_for_king(self, position, game):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if game.board[curr_index[0]][curr_index[1]] == ['K', self.player_color]:
            print(f'A map of your possible moves for king at position {position}:')
            move_set_list = King_possible_moves(game, curr_index)

            move_map = copy.deepcopy(game)
            for move in move_set_list:
                move_map.board[move[0]][move[1]] = '*'
            return move_map.get_board()


    def possible_moves_for_queen(self, position, game):
        curr_let = [loc for loc in position]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        if game.board[curr_index[0]][curr_index[1]] == ['Q', self.player_color]:
            print(f'A map of your possible moves for queen at position {position}:')
            move_set_list = Queen_possible_moves(game, curr_index)

            move_map = copy.deepcopy(game)
            for move in move_set_list:
                move_map.board[move[0]][move[1]] = '*'
            return move_map.get_board()


    def move_pawn(self, position_from, position_to, game):
        curr_let = [loc for loc in position_from]
        next_let = [loc for loc in position_to]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        next_index = [rank.index(next_let[1]), file.index(next_let[0])]
        move_set_list = Pawn_possible_moves(game, curr_index, self.player_color)

        if next_index in move_set_list:
            move_piece(game, curr_index, next_index)
            print(f'Pawn at {position_from} has been moved to {position_to}')

        return True

    
    def move_rook(self, position_from, position_to, game):
        curr_let = [loc for loc in position_from]
        next_let = [loc for loc in position_to]
        curr_index = [rank.index(curr_let[1]), file.index(curr_let[0])]
        next_index = [rank.index(next_let[1]), file.index(next_let[0])]
        move_set_list = Rook_possible_moves(game, curr_index)

        if next_index in move_set_list:
            move_piece(game, curr_index, next_index)
            print(f'Rook at {position_from} has been moved to {position_to}')

        return True


def Rook_possible_moves(game, index):
    move_set_list = []

    ptr = index
    while ptr[0] > 0:
        ptr = [ptr[0] - 1, ptr[1]]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)
        else:
            break

    ptr = index
    while ptr[0] < len(rank) - 1:
        ptr = [ptr[0] + 1, ptr[1]]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)
        else:
            break

    ptr = index
    while ptr[1] > 0:
        ptr = [ptr[0], ptr[1] - 1]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)
        else:
            break
    
    ptr = index
    while ptr[1] < len(file) - 1:
        ptr = [ptr[0], ptr[1] + 1]
        if game.board[ptr[0]][ptr[1]] == ' ':
            move_set_list.append(ptr)

    return move_set_list


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

    return move_set_list


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
    
    return move_set_list


def King_possible_moves(game, index):
    move_set_list_cross = Rook_possible_moves(game, index)
    move_set_list_diagonal = Bishop_possible_moves(game, index)
    move_set_list = move_set_list_cross + move_set_list_diagonal

    move_map = copy.deepcopy(game)
    for move in move_set_list:
        move_map.board[move[0]][move[1]] = '*'
    return move_set_list

def Queen_possible_moves(game, index):
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
                if game.board[ptr[0] - 1][file_i] == ' ':
                    move_set_list.append([ptr[0] - 1, file_i])

    # Black pawn's moves
    if color == "Black" and ptr[0] < len(rank):
        # bottom two diagonal blocks of current index
        for file_i in range(ptr[1] - 1, ptr[1] + 2, 2):
            if file_i >= 0 and file_i < len(file):
                if game.board[ptr[0] + 1][file_i] == ' ':
                    move_set_list.append([ptr[0] + 1, file_i])

    return move_set_list


def move_piece(game, index_from, index_to):
    temp = game.board[index_from[0]][index_from[1]]
    game.board[index_from[0]][index_from[1]] = ' '
    game.board[index_to[0]][index_to[1]] = temp