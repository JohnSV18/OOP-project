from car import Owner
from showcase import Showcase

class Skills: 
    def __init__(self, jump_height) :
        self.jump_height = jump_height

    def jump(self, high_jump):
        high_jump = (high_jump / 2)
        self.points += high_jump

        return self.points
    
    def flip(self, num_of_flips):
        self.points += num_of_flips * 2
    
    

        











   
