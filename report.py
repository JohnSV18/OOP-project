from weather import Weather
from rain import Rain
from sun import Sun
# this class is Report and is where we will ask the user for some information and then also give some tips based on the info given

class Report:
    def __init__(self):
        # this is an empty list which will hold each forecast after we create them
        self.daily_forecast = list()
    # this method will ask the user for some information and then create a Rain object 
    # the object will then be added to the list that was made above
    def add_rain(self):
        temperature = input("I see it's windy but what is the temperature? ")
        sky = input("How is the sky looking? ")
        is_thunder_storm = input("Is there a thunderstorm outside? (True or False) ")
        flood_level = input('Out of 10, what is the flood level? ')
        
        new_rain = Rain(temperature, is_thunder_storm, sky, flood_level)
        self.daily_forecast.append(new_rain)
    # this method will ask the user for some information and then create a Sun object 
    # the object will then be added to the list that was made above
    def add_sun(self):

        temperature = input("I see it's hot but what is the temperature? ")
        sky = input("How is the sky looking? ")
        is_over_90 = input("Is it over 90 degrees? (True or False) ")

        new_sun = Sun(temperature, is_over_90, sky)
        self.daily_forecast.append(new_sun)
    
    # this method will show you the forecast based on all the information you put in 
    # it will loop through the list and print out the temperature for that day and the sky description
    def show_forecast(self):
        counter = 1

        for forecast in self.daily_forecast:
            print('-------------------')
            print("Day " + str(counter) + ' forecast: ')
           
            print('Temperature: ' + str(forecast.temperature))
            print('The sky is looking ' + str(forecast.sky))
            print('-------------------')
          
            
            counter += 1
        #after the loop the user will then be asked if they want some tips
        asking_tips = input("Would you like some tips?")
        
        if asking_tips == "yes":
            counter_2 = 1
            # if the user inputs 'yes' then the tips for each day will be displayed based on the information given for each day.
            for forecast in self.daily_forecast:
                
                # import pdb; pdb.set_trace()
                print('DAY ' + str(counter_2))
                forecast.what_is_the_weather()
                forecast.should_wear_jacket()
                forecast.is_flooding()
                forecast._heat_wave()

                counter_2 += 1
               
                
        


    # test
# Weather = Rain(60, "cloudy")
# report = Report(Weather)
# report.get_report()


report = Report()
report.add_sun()
report.add_rain()

report.show_forecast()

