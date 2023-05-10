import chess

game = chess.Chess()
p1 = chess.Player1(game, 'p1')
p2 = chess.Player2(game, 'p2')
p1.update_player()
p2.update_player()
game.setup_board()
print(game.select_player())
p1.move_pawn('a2', 'b3')
p2.move_pawn('h7', 'g6')
p1.possible_moves_for_rook('a1')
p2.possible_moves_for_rook('h8')