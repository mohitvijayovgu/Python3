from main import weather_check

# Test cases for weather_check function

def test_weather_check():
    assert weather_check(-5) == "Its Freezing outside"
    assert weather_check(10) == "Its bit chilly outside"
    assert weather_check(20) == "The weather is pleasant outside"


if __name__ == "__main__":
    test_weather_check()
    print("All tests passed!")