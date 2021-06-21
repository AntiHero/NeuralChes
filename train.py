import os
import chess.pgn

for file in os.listdir("data"):
    pgn = open(os.path.join("data", file))

while 1:
    try:
        game = chess.pgn.read_game(pgn)
    except Exception:
        break
    print(game)
