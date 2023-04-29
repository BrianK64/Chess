# Chess
Built a game of Chess using Python

This Python code includes three main clasees - Chess, Player1, and Player2.
These classes are independent of each other (none of them are parent of another or child of another),
but interact with each other by directly calling objects' instances.

Description for Chess class:
  This class is mainly for creating a board, setting up the board, and selecting each player's color and who starts first.
  This class does not take in any arguments but records instances like board, player1, player2, each player's color.
  
 Description for Player1 and Player2 class:
  Takes in player's name, and a Chess object to keep track of current game.
  Player1 can see possible moves for each type of pieces in Chess.
  Player1 can also move a piece player wants to move and update the board.
  
  
  #Things to note: 
    In the game of Chess, board is consisted of ranks(rows) and files(columns).
    The board goes rank 1 through rank 8 from bottom to top, and file a to file h from left to right.
    However, two dimensional arrays in coding counts rows from top to bottom, that is, 
    rank 1 on chess board would be 7th row element of the array and rank 8 would be 0th row element.
  
  
  note on 04/29/2023
    - Might add classes for each piece to handle possible moves and moving the piece.
      - This way, we can just call the function in player class to figure out what to move and how to move depending on the color the player is assigned.
