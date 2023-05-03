import chess

game = chess.Chess()
p1 = chess.Player1('p1')
p2 = chess.Player2('p2')
p1.update_player(game)
p2.update_player(game)
game.setup_board()
print(game.select_player())
p1.get_color(game)

p1.possibe_moves_for_rook('a1', game)
p1.possible_moves_for_bishop('f1', game)
p1.possible_moves_for_knight('g1', game)
p1.possible_moves_for_king('d1', game)
p1.possible_moves_for_queen('e1', game)
p1.possible_moves_for_pawn('h2', game)
