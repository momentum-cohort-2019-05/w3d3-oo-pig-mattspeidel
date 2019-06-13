Class name: Game
Responsibilities: Runs the gamestate loop, determines the turn order, checks for a winner, asks if you want to play again.
Collaborators: Player, AI

Class name: Player
Reponsibilities: Check to see if player want to roll or hold, checks for bust, calculates score
Collaborators: Game, AI

Class name: AI
Responsibilities: Continues rolling until getting at least 20 then will hold, otherwise bust, calculates score
Collaborators: Game, Player