def filter_by_age(players, max_age):
    less_than_max_age = []
    for player in players:
        if player.age < max_age:
            less_than_max_age.append(player)
    return less_than_max_age

def filter_by_rating(players, min_rating):
    at_least_min_rating = []
    for player in players:
        if player.rating >= min_rating:
            at_least_min_rating.append(player)
    return at_least_min_rating
