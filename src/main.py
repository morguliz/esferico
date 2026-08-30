from player import Player
# test
bellingham = Player("Jude Bellingham", 23, "Real Madrid", "La Liga", "AM", 1917, 6, 4, 7.53)
vinicius = Player("Vinicius Junior", 26, "Real Madrid", "La Liga", "LF", 2825, 16, 5, 7.65)
valverde = Player("Federico Valverde", 28, "Real Madrid", "La Liga", "RB", 2746, 5, 8, 7.60)
mbappe = Player("Kylian Mbappe", 27, "Real Madrid", "La Liga", "ST", 2604, 25, 5, 8.02)

print(bellingham.goals_per_90())
print(bellingham.assists_per_90())

print(bellingham.goals)
print(vinicius.name)
print(valverde.rating)
print(mbappe.minutes)

players = [bellingham, vinicius, valverde, mbappe]
for player in players:
    print(player.name)

for player in players:
    if player.age < 25:
        print(player.name)

current_best = players[0]
for player in players:
    if player.rating > current_best.rating:
        current_best = player
print(current_best.name)

for player in players:
    if player.age < 28 and player.rating >= 7.60:
        print("under 28 AND have a rating of at least 7.6: " + player.name)

'''    goals per 90     '''
for player in players:
    goals_per_90 = player.goals / player.minutes * 90
    print(round(goals_per_90, 3))

for player in players:
    if player.age < 25 and player.goal_contributions_per_90() >= 0.50:
        print(player.name)