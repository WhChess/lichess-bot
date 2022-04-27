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
        print("========================")
        print("Hamlem:", a)
        board = chess.Board(board.fen())
        if board.is_checkmate():
            print("OYUN BİTTİ!")
            break;
        print("========================")
        legal_moves = list(board.legal_moves)
        a1 = random.choice(legal_moves)
        b = input("Lütfen bir hamle seçin: ")
        while True:
            try:
                board.push_san(b)
                break;
            except:
                if(b=="R"):
                    board.push(a1)
                    print("Rastgele yaptığım hamle:",a1)
                    break;
                b = input("Lütfen hamleyi doğru seçin: ")
        print("========================")
        board = chess.Board(board.fen())
        if board.is_checkmate():
            print("OYUN BİTTİ!")
            break;
asyncio.run(main())