
class Weather:
# takes the temperture (int) and how the sky looks (string)
    def __init__(self, temperature, sky):
        self.temperature = temperature
        self.sky = sky

        # this method adds too global warming and increases temp by 20
    def addGlobalWarming(self):
        self.temperature += 20
        print(self.temperature)
#  this method will return true or false to wearing a jacket depending on sky input
    def shouldWearJacket(self):
        if self.sky == 'sunny':
            print('No need for a jacket')
        else:
            print('wear your jacket')
    # this method prints a string (Doesn't know weather)
    def what_is_the_weather(self):
        print('I dont know the current weather')



        # test

# weather = Weather(30, 'cloudy')
# weather.addGlobalWarming()
# weather.shouldWearJacket()
# weather.what_is_the_weather()
