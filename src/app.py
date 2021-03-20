import json
from flask import Flask
from flask import request, redirect
from src.input.processor import InputProcessor
from icecream import ic

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return redirect("https://github.com/grigorjevas/Discogs-price-prediction")


@app.route("/predict/", methods=["POST"])
def predict() -> [str, int]:
    """
    Reads and validates the data from POST request, predicts Discogs Marketplace item price.

    :return: http response with json
    """
    try:
        request_data = json.loads(request.data)
    except ValueError:
        return json.dumps({"response": "error", "msg": "Invalid json format"})

    input_processor = InputProcessor(request_data)

    validation = input_processor.validate
    if validation["response"] == "ok":
        prediction = input_processor.predict
        return json.dumps(prediction), 200
    return json.dumps(validation), 400

