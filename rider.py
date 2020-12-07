from bike import Bike

class Rider(Bike):
    def __init__(self, name, energy = 100):
        self.name = name
        self._energy = energy
    
    def energy_bar(self, num_bars):
        if num_bars > 0:
            self.energy += 2

    
    
    


    



    
