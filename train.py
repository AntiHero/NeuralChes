import os
import chess.pgn

for fn in os.listdir("data"):
    print(fn)
    pgn = open(os.path.join("data", fn))

while 1:
    try:
        game = chess.pgn.read_game(pgn)
    except Exception:
        break
    print(game)
