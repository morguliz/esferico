class Player:
    def __init__(self, name, age, club, league, position, minutes, goals, assists, rating):
        self.name = name
        self.age = age
        self.club = club
        self.league = league
        self.postition = position
        self.minutes = minutes
        self.goals = goals
        self.assists = assists
        self.rating = rating
# test
bellingham = Player("Jude Bellingham", 23, "Real Madrid", "La Liga", "AM", 1917, 6, 4, 7.53)
vinicius = Player("Vinicius Junior", 26, "Real Madrid", "La Liga", "LF", 2825, 16, 5, 7.65)
valverde = Player("Federico Valverde", 28, "Real Madrid", "La Liga", "RB", 2746, 5, 8, 7.60)
mbappe = Player("Kylian Mbappe", 27, "Real Madrid", "La Liga", "ST", 2604, 25, 5, 8.02)

print(bellingham.goals)
print(vinicius.name)
print(valverde.rating)
print(mbappe.minutes)

players = [bellingham, vinicius, valverde, mbappe]
for player in players:
    print(player.name)