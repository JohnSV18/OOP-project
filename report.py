from weather import Weather
from rain import Rain
from sun import Sun

class Report:
    def __init__(self):
        self.weekly_forecast = list()

    def add_rain(self,temperature, is_thunder_storm, sky, water_level):
        new_rain = Rain(temperature, is_thunder_storm, sky, water_level)
        self.weekly_forecast.append(new_rain)

    def add_sun(self, temperature, is_over_90, sky):
        new_sun = Sun(temperature, is_over_90, sky)
        self.weekly_forecast.append(new_sun)
    # this method prints out doesn't know what the weather is
    def get_report(self):
        weather.what_is_the_weather()
    # this method adds the global warming  and
    def include_global_warming_projection(self):
        weather.addGlobalWarming()
        weather.what_is_the_weather()
        weather.shouldWearJacket()

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
report.add_sun(98, True, "cloudy")
report.add_sun(100, True, "Sunny")
report.add_sun(97, True, "partially cloudy")
report.add_sun(90, False, "cloudy")
report.add_sun(92, True, "foggy")

report.show_forecast()
