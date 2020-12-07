from car import Dog
class Showcase:
    def __init__(self, points=0):
        self.points = points
    

    def check_years_trained(self):
        if self.years_trained >= 2:
            self.points += 2
        elif self.years_trained > 2 and < 5:
            self.points += 4
        elif self.years_trained > 5:
            self.points += 6

    def check_points(self):

        print(self.points)