def filter_by_age(players, max_age):
    less_than_max_age = []
    for player in players:
        if player.age < max_age:
            less_than_max_age.append(player)
    return less_than_max_age
