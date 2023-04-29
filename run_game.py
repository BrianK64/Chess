import chess

game = chess.Chess()
p1 = chess.Player1('p1')
p2 = chess.Player2('p2')
p1.update_player(game)
p2.update_player(game)
game.setup_board()
print(game.select_player())