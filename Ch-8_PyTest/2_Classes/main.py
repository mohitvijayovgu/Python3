class weather():
    
    def weather_check(self, temp: float)->str:
        if temp <0:
            return "Its Freezing outside"
        elif temp < 15:
            return "Its bit chilly outside"
        elif temp < 25:
            return "The weather is pleasant outside"
        else:
            return "Its Hot outside"
        
    def rain_check(self, rain_chance):
        if rain_chance > 0.7:
            return "Its likely to rain. Dont forget your umbrella!"
        elif rain_chance > 0.3:
            return "There is a chance of rain. You might want to carry an umbrella."
        else:
            return "Its unlikely to rain today."