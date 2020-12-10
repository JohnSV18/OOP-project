from weather import Weather
class Rain(Weather):
    def __init__(self, temperature, is_thunder_storm, sky, water_level):
        self.is_thunder_storm = is_thunder_storm
        self.water_level = water_level
        Weather.__init__(self,temperature, sky)
    # this method prints a string explaing it's raining and the temp as well
    def what_is_the_weather(self):
        print('The weather is rainy with a temp of' + self.temperture)

    def flooding(self):
        if self.water_level > 5:
            print('Stay home there is a flood outside')
        else:
            print('There is no flood yet but just becareful')
            
