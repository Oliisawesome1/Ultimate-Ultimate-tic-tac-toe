HOW TO PLAY:

each 3x3 grid of squares is its own game of tic-tac-toe.
if you get three in a row in the game it will become a X or O in the next game up.
First to get 3 in a row in the largest game wins!

X starts by selecting any square, this square will then determine which game O goes to. 
This is best explained by imagining the window you put your square in as the whole collection of them,
and the square you chose being the game.

The coords are [window][game][square].
So if you go in [1][4][3] your opponent next move will go to [4][3][their choice]
You will then go to [3][their choice][your choice]

The exception to this rule is if the game the player will go to is full.
Then the other player can pick any game in the window.
[1][4][3] will go to [4][ANY][ANY]

This also applies when a window is full, the other player can go anywhere at all.
