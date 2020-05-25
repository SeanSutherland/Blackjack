from Game import Game
cash = 10000
print("How many shoe's would you like to go through?")
games = int(input())
for i in range(games):
    game = Game(cash)
    cash = game.player.cash

print ("Cash: " + str(game.player.cash) + "\nGain: " + str(float((cash/(10000) -1)*(100/games))) + "% \nGames: " + str(games))
