
class Weather:
# takes the temperture (int) and how the sky looks (string)
    def __init__(self, temperature, sky):
        self.temperature = temperature
        self.sky = sky

        # this method adds too global warming and increases temp by 20
    def addGlobalWarming(self):
        self.temperature += 20
#  this method will return true or false to wearing a jacket depending on sky input
    def shouldWearJacket(self):
        if sky == 'sunny':
            return False
        else:
            return True
    # this method prints a string (Doesn't know weather)
    def what_is_the_weather(self):
        print('I dont know the current weather')
