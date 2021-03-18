import pickle
import json
from flask import Flask
from flask import request, redirect
from icecream import ic

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return redirect("https://github.com/grigorjevas/Discogs-price-prediction")


@app.route("/predict/", methods=["POST"])
def predict() -> str:
    """
    Reads the data from POST request, predicts Discogs Marketplace item price.

    :return:
    """
    input_params = request.data
    ic(input_params)
    return input_params["test"]
