from weather import Weather

class Sun(Weather):
    def __init__(self, temperature, is_over_90, sky):
        self.is_over_90 = is_over_90
        Weather.__init__(self,temperature, sky)

    def what_is_the_weather(self):
        if self.is_over_90:
            print('Go to the beach!')
        else:
            print('Today is sunny and is ' + self.temperature )
