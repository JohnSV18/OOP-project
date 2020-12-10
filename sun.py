from weather import Weather

class Sun(Weather):
    def __init__(self, temperature, is_over_90, sky):
        Weather.__init__(self,temperature, sky)
        self.is_over_90 = is_over_90

    def what_is_the_weather(self):
        if self.is_over_90 is True:
            print('Please wear sunscreen!')
        else:
            print('Today is below 90. The tempereature is ' + str(self.temperature) )

# test
# sun = Sun(60, False, "clear")
# sun.what_is_the_weather()