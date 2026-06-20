from main import api_calls
import pytest

def test_api_calls(mocker):
    mocker_get  = mocker.patch("main.requests.get")
    mocker_get.return_value.json.return_value = {"main": {"key": "value"}}

    result = api_calls("https://api.openweathermap.org/data/2.5/weather?q=London&appid=your_api_key")
    assert result == {"data": {"main": {"key": "value"}}}

