import json
from flask import Flask
from flask import request, redirect
from src.input.processor import InputProcessor
from src.database.queries import Queries

app = Flask(__name__)
db_query = Queries()


def __init__():
    db_query.create_tables()


@app.route("/", methods=["GET"])
def index() -> str:
    """
    Redirects to project github page

    :return: http response with redirect url
    """
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
        db_query.log_prediction(request_data, prediction)
        return json.dumps(prediction), 200
    return json.dumps(validation), 400


@app.route("/history/", defaults={"num_items_to_show": 10}, methods=["GET"])
@app.route("/history/<num_items_to_show>", methods=["GET"])
def show_history(num_items_to_show: int) -> [str, int]:
    """
    Returns a specified number of successful price predictions. Default =  10.

    :param num_items_to_show:
    :return: http response with json
    """
    return json.dumps({"prediction_history": db_query.get_predictions(num_items_to_show)}), 200
