import pytest
from src.input.validator import InputValidator
from src.input.processor import InputProcessor
from src.database.database import Database
import requests


valid_data_example = {
  "artist": "DMX Krew",
  "title": "Dread It A Go EP",
  "release_format": "LP",
  "number_of_tracks": 8,
  "release_year": 2002,
  "rating": 4.75,
  "votes": 24,
  "have": 111,
  "want": 106,
  "limited_edition": True,
  "media_condition": 5,
  "sleeve_condition": 4
}

invalid_data_example = {
  "artist": 666,
  "title": "Dread It A Go EP",
  "release_format": "LP",
  "number_of_tracks": 8,
  "release_year": 2002,
  "rating": 4.75,
  "votes": 24,
  "have": 111,
  "want": 106,
  "limited_edition": True,
  "media_condition": 5,
  "sleeve_condition": 4
}


def test_validator_valid():
    validator = InputValidator(valid_data_example)
    validate = validator.validate_input
    assert validate["response"] == "ok"


def test_validator_invalid():
    validator = InputValidator(invalid_data_example)
    validate = validator.validate_input
    assert validate["response"] == "error"


def test_processor_validate():
    input_processor = InputProcessor(valid_data_example)
    validation = input_processor.validate
    assert validation["response"] == "ok"


def test_predict():
    input_processor = InputProcessor(valid_data_example)
    result = input_processor.predict
    assert pytest.approx(True, 19) == result["predicted_price"]


def test_get_history():
    url = "https://discogs-price-prediction.herokuapp.com/history"
    response = requests.get(url)
    history = response.json()
    assert (len(history["prediction_history"]) == 10)
