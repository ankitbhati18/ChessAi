import chess
import chess.engine

class ChessAI:
    def __init__(self, depth=3):
        self.depth = depth

    def evaluate_board(self, board):
        # Simple evaluation function
        if board.is_checkmate():
            return -9999 if board.turn else 9999
        return sum(self.get_piece_value(piece) for piece in board.piece_map().values())

    def get_piece_value(self, piece):
        values = {
            chess.PAWN: 100,
            chess.KNIGHT: 300,
            chess.BISHOP: 300,
            chess.ROOK: 500,
            chess.QUEEN: 900,
            chess.KING: 10000
        }
        return values.get(piece.piece_type, 0)

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        if depth == 0 or board.is_game_over():
            return self.evaluate_board(board)

        if maximizing_player:
            max_eval = float('-inf')
            for move in board.legal_moves:
                board.push(move)
                eval = self.minimax(board, depth - 1, alpha, beta, False)
                board.pop()
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in board.legal_moves:
                board.push(move)
                eval = self.minimax(board, depth - 1, alpha, beta, True)
                board.pop()
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def get_best_move(self, board):
        best_move = None
        best_value = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            move_value = self.minimax(board, self.depth - 1, float('-inf'), float('inf'), False)
            board.pop()
            if move_value > best_value:
                best_value = move_value
                best_move = move
        return best_move

# Example usage
if __name__ == "__main__":
    board = chess.Board()
    ai = ChessAI(depth=3)

    while not board.is_game_over():
        print(board)
        if board.turn:  # AI's turn
            move = ai.get_best_move(board)
            board.push(move)
        else:  # Human player's turn
            user_move = input("Enter your move: ")
            board.push(chess.Move.from_uci(user_move))