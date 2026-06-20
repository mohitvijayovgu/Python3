from main import weather_check
import pytest


@pytest.mark.parametrize("temp, expected", [
    (-5, "Its Freezing outside"),
    (10, "Its bit chilly outside"),
    (20, "The weather is pleasant outside"),
    (30, "Its Hot outside")
])
# Test cases for weather_check function

def test_weather_check(temp, expected):
    assert weather_check(temp) == expected


if __name__ == "__main__":
    test_weather_check()
    print("All tests passed!")