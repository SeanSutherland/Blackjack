from Game import Game
cash = 10000
for i in range(100):
    game = Game(cash)
    cash = game.player.cash
