from player import Player
from filters import filter_by_age
from filters import filter_by_rating
# sample player data
bellingham = Player("Jude Bellingham", 23, "Real Madrid", "La Liga", "AM", 1917, 6, 4, 7.53)
vinicius = Player("Vinicius Junior", 26, "Real Madrid", "La Liga", "LF", 2825, 16, 5, 7.65)
valverde = Player("Federico Valverde", 28, "Real Madrid", "La Liga", "RB", 2746, 5, 8, 7.60)
mbappe = Player("Kylian Mbappe", 27, "Real Madrid", "La Liga", "ST", 2604, 25, 5, 8.02)


players = [bellingham, vinicius, valverde, mbappe]
seven_six = filter_by_rating(players, 7.60)
for player in seven_six:
    print(player.name)


