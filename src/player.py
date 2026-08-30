class Player:
    def __init__(self, name, age, club, league, position, minutes, goals, assists, rating):
        self.name = name
        self.age = age
        self.club = club
        self.league = league
        self.position = position
        self.minutes = minutes
        self.goals = goals
        self.assists = assists
        self.rating = rating

    def goals_per_90(self):
        return round(self.goals / self.minutes * 90, 3)
    def assists_per_90(self):
        return round(self.assists / self.minutes * 90, 3)
    def goal_contributions_per_90(self):
        return round(self.goals_per_90() + self.assists_per_90(), 4)