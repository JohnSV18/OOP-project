from weather import Weather
from rain import Rain
from sun import Sun

class Report:
    def __init__(self):
        self.weekly_forecast = list()

    def add_rain(self,temperature, is_thunder_storm, sky, flood_level):
        
        new_rain = Rain(temperature, is_thunder_storm, sky, flood_level)
        self.weekly_forecast.append(new_rain)

    def add_sun(self):
        
        temperature = input("What is the temperature? ")
        sky = input("How is the sky looking? ")
        is_over_90 = input("Is it over 90 degrees? (True or False) ")

        new_sun = Sun(temperature, is_over_90, sky)
        self.weekly_forecast.append(new_sun)
    # this method prints out doesn't know what the weather is
    def get_report(self):
        Weather.what_is_the_weather()
    # this method adds the global warming  and
    def include_global_warming_projection(self):
        for forecast in self.weekly_forecast:

            forecast.addGlobalWarming()
            forecast.what_is_the_weather()
            forecast.shouldWearJacket()

    def show_forecast(self):
        counter = 1
        for forecast in self.weekly_forecast:

            print("Day " + str(counter) + ' forecast: ')
            print('Temperature: ' + str(forecast.temperature))
            print('The sky is looking ' + str(forecast.sky))
            
            counter += 1


    # test
# Weather = Rain(60, "cloudy")
# report = Report(Weather)
# report.get_report()
report = Report()
report.add_sun()
report.add_rain(50, True, "Thunder", 5 )
# report.add_sun(90, False, "cloudy")
report.add_rain(92, True, "foggy", 6)
report.show_forecast()
# report.include_global_warming_projection
