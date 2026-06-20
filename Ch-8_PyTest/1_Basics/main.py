def weather_check(temp:float) -> str:
    if temp < 0:
        return "Its Freezing outside"
    elif temp < 15:
        return "Its bit chilly outside"
    elif temp < 25:
        return "The weather is pleasant outside"
    else:
        return "Its Hot outside"
    
print(weather_check(10))