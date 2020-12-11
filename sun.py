from weather import Weather
# this is the Sun class which includes the atrributes that let you know the temperature, how the sky looks, and if the temperature is over 90
# The weather class is inherited by Sun
class Sun(Weather):
    def __init__(self, temperature, is_over_90, sky):
        Weather.__init__(self,temperature, sky)
        self.is_over_90 = is_over_90
    # This method will take in what the user inserts after the question "is it over 90?" and based on the input will print out a tip
    def what_is_the_weather(self):
        if self.is_over_90 == 'True' or self.is_over_90 == 'true':

            print('----------------------')
            print('Please wear sunscreen!')
            print('----------------------')
        else:
            print('----------------------')
            print('Today is below 90. The tempereature is ' + self.temperature )
            print('----------------------')
    # this method will take in what the user inserts for "is it over 90?" and based on that will print out another tip notifying you if there is a heatwave
    # this method is also protected because we only want to be able to have access in the subclasses which are Rain and Sun
    def _heat_wave(self):
        if self.is_over_90 == 'True':
            print('----------------------')
            print('There is a heat wave')
            print('----------------------')
        else:
            print('----------------------')
            print('Weather is mellow, no heatwave today')
            print('----------------------')
    #this method is an empty method but is protected because we only want to be able to have access in the subclasses which are Rain and Sun
    def is_flooding(self):
        pass

# test
# sun = Sun(60, False, "clear")
# sun.what_is_the_weather()