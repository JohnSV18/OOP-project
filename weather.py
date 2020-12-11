# this is the weather class which takes the temperture (int) and how the sky looks (string)
class Weather:
    def __init__(self, temperature, sky):
        self.temperature = temperature
        self.sky = sky

#  this method will give you a tip on if you should wear a jacket based on the input the user puts for when asked to describe how the sky looks
    def should_wear_jacket(self):
        if self.sky == 'sunny' or self.sky == 'Sunny':
            print('----------------------')
            print('No need for a jacket')
            print('----------------------')
        else:
            print('----------------------')
            print('wear your jacket if going outside')
            print('----------------------')
    # this method prints a string (Doesn't know weather)
    # this method is also over written in some cases from the subclasses Rain and Sun
    def what_is_the_weather(self):
        print('----------------------')
        print('I dont know the current weather')
        print('----------------------')



        # test

# weather = Weather(30, 'cloudy')
# weather.addGlobalWarming()
# weather.shouldWearJacket()
# weather.what_is_the_weather()
