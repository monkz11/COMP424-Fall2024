# Student agent: Add your own agent here
from agents.agent import Agent
from store import register_agent
import sys
import numpy as np
from copy import deepcopy
import time
from helpers import random_move, count_capture, execute_move, check_endgame, get_valid_moves

@register_agent("student_agent")
class StudentAgent(Agent):
  """
  A class for your implementation. Feel free to use this class to
  add any helper functionalities needed for your agent.
  """

  def __init__(self):
    super(StudentAgent, self).__init__()
    self.name = "StudentAgent"

  def step(self, chess_board, player, opponent):
    """
    Implement the step function of your agent here.
    You can use the following variables to access the chess board:
    - chess_board: a numpy array of shape (board_size, board_size)
      where 0 represents an empty spot, 1 represents Player 1's discs (Blue),
      and 2 represents Player 2's discs (Brown).
    - player: 1 if this agent is playing as Player 1 (Blue), or 2 if playing as Player 2 (Brown).
    - opponent: 1 if the opponent is Player 1 (Blue), or 2 if the opponent is Player 2 (Brown).

    You should return a tuple (r,c), where (r,c) is the position where your agent
    wants to place the next disc. Use functions in helpers to determine valid moves
    and more helpful tools.

    Please check the sample implementation in agents/random_agent.py or agents/human_agent.py for more details.
    """

    # Some simple code to help you with timing. Consider checking 
    # time_taken during your search and breaking with the best answer
    # so far when it nears 2 seconds.
    start_time = time.time()
    time_taken = time.time() - start_time

    #print("My AI's turn took ", time_taken, "seconds.")

    # Dummy return (you should replace this with your actual logic)
    # Returning a random valid move as an example
    # greedy solution
    total_count = 0
    best_move = ()
    set_moves = get_valid_moves(chess_board,player)
    corner_cases = [(0,1),(1,0),(1,1),(0, len(chess_board)-2), (1, len(chess_board)-2), (1, len(chess_board)-1),(len(chess_board)-1,1), (len(chess_board)-2,0), (len(chess_board)-2,1), (len(chess_board)-2,len(chess_board)-2), (len(chess_board)-2,len(chess_board)-1), (len(chess_board)-1,len(chess_board)-1)]

    for corner_moves in set_moves:
      if len(set_moves) > 1 and (corner_moves in corner_cases):
        set_moves.remove(corner_moves)

      
    for valid_move in set_moves:

      opponent = 3 - player
      r, c = valid_move
      directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                    (-1, -1), (-1, 1), (1, -1), (1, 1)] 

      def count_in_direction(dr, dc):
          """Count flips in a single direction."""
          flips = 0
          i, j = r + dr, c + dc
          while 0 <= i < len(chess_board) and 0 <= j < len(chess_board[0]) and chess_board[i][j] == opponent:
              flips += 1
              i += dr
              j += dc
          if 0 <= i < len(chess_board) and 0 <= j < len(chess_board[0]) and chess_board[i][j] == player:
              return flips
          return 0

      if chess_board[r][c] != 0:
          return 0

      total_flips = sum(count_in_direction(dr, dc) for dr, dc in directions)



      if total_flips > total_count:
        total_count = total_flips
        best_move = valid_move
        
      
    return best_move

