import chess
import random
import asyncio

async def main():
    board = chess.Board()
    while True:
        legal_moves = list(board.legal_moves)
        a = random.choice(legal_moves)
        await asyncio.sleep(2)
        board.push(a)
        print(board)
        board = chess.Board(board.fen())
        if board.is_checkmate():
            print("OYUN BİTTİ!")
            break;
        print("========================")
        legal_moves = list(board.legal_moves)
        a = random.choice(legal_moves)
        b = input("Lütfen bir hamle seçin: ")
        while True:
            if(b == "R"):
                board.push(a)
                break;
            else:
                while True:
                    try:
                        board.push_san(b)
                        break;
                    except:
                        b = input("Lütfen hamleyi doğru seçin: ")
        print("========================")
        board = chess.Board(board.fen())
        if board.is_checkmate():
            print("OYUN BİTTİ!")
            break;
asyncio.run(main())