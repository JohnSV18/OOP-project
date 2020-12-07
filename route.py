import random
from bike import Bike
from rider import Rider

class Route(Rider):
    def __init__(self, road_type, length, potholes = 0):
        # potholes will slow you down even if you are just avoiding them and don't fall into one
        self.potholes = potholes
        # a very flat route will help you with speed
        self.road_type = road_type
        # a heavier bike woould't go as fast
        self.length = length

    def jump(self, jump):
        if jump is True and self.ebike is False:
            self.speed -= 3

    def turn(self, swerve = False):
        if swerve is True:
            self.speed -= 1
    
    def weather(self, windspeed):
        if windspeed > 0:
            self.speed += windspeed
        print(self.speed)
    
    def add_potholes(self):
        self.potholes += random.randint(0, 5)


hey = Bike( 30, 30, False)
yo = hey.turn()

print(hey.weight)
print(hey.speed)










   
