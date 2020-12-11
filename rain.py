from weather import Weather

# This is the Rain class which includes the atrributes that let you know water level or if there is a thunderstorm or not.
# The weather class is inherited by Rain
class Rain(Weather):
    def __init__(self, temperature, is_thunder_storm, sky, water_level):
        self.is_thunder_storm = is_thunder_storm
        self.water_level = water_level

        Weather.__init__(self,temperature, sky)
    # this method prints out a tip with the temperature also for a Rain object
    # this method is public because we can access it here or even in the weather class
    # this method overrides the 'what_is_the_weather' method in the weather class
    def what_is_the_weather(self):
        print('Here are some tips!')
        print('The weather is rainy with a temp of ' + self.temperature)
        print('----------------------')
    # this method will take in the user input for the question "Is there a thunderstorm?" and then print out a tip based on the input
    def is_flooding(self):
        if self.is_thunder_storm == 'True' or self.is_thunder_storm == 'true':
            print('----------------------')
            print('Stay home it is raining outside and the flood level is ' + self.water_level)
            print('----------------------')
        else:
            print('----------------------')
            print('There is a slight flood but just becareful')
            print('----------------------')
    #this method is an empty method but is protected because we only want to be able to have access in the subclasses which are Rain and Sun
    def _heat_wave(self):
        pass


