from main import weather

def test_weather_check():
    w = weather()
    assert w.weather_check(-5) == "Its Freezing outside"
    assert w.weather_check(10) == "Its bit chilly outside"
    assert w.weather_check(20) == "The weather is pleasant outside"
    assert w.weather_check(30) == "Its Hot outside"

def test_rain_check():
    w = weather()
    assert w.rain_check(0.8) == "Its likely to rain. Dont forget your umbrella!"
    assert w.rain_check(0.5) == "There is a chance of rain. You might want to carry an umbrella."
    assert w.rain_check(0.2) == "Its unlikely to rain today."