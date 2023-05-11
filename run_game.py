import chess

game = chess.Chess()
p1 = chess.Player1(game, 'p1')
p2 = chess.Player2(game, 'p2')
p1.update_player()
p2.update_player()
game.setup_board()
print(game.select_player())