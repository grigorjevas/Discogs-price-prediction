import pickle
import numpy as np
from src.util.input_validator import InputValidator


class InputProcessor:
    """
    Class to process the input data and make predictions about prices.

    Available methods:
        * validate - validates the input using InputValidator class
        * predict - predicts the record price
    """

    def __init__(self, input_data: dict) -> None:
        self.__input_data = input_data
        self.__one_hot_encoder = pickle.load(open("models/one_hot_encoder.pkl", "rb"))
        self.__scaler = pickle.load(open("models/scaler.pkl", "rb"))
        self.__model = pickle.load(open("models/model.pkl", "rb"))

    @property
    def validate(self) -> dict:
        """
        Uses the InputValidator class to validate the data.

        :return: json response ok or errors
        """
        validate = InputValidator(self.__input_data)

        if not validate.validate_keys["response"] == "ok":
            return validate.validate_keys

        if not isinstance(validate.validate_input, bool):
            return validate.validate_input

        return {"response": "ok"}

    @property
    def encode(self) -> np.array:
        """
        Prepares the data to be used in the model by encoding categorical data and scaling numerical data.

        :return: numpy array
        """
        encoded_data = self.__one_hot_encoder.transform([[self.__input_data["release_format"]]]).todense()
        numeric_data = [
            self.__input_data["number_of_tracks"],
            self.__input_data["rating"],
            self.__input_data["votes"],
            self.__input_data["have"],
            self.__input_data["want"],
            self.__input_data["limited_edition"],
            self.__input_data["media_condition"],
            self.__input_data["sleeve_condition"],
            self.__input_data["release_year"]
        ]
        scaled_data = self.__scaler.transform([numeric_data])
        encoded_features = np.concatenate([encoded_data, scaled_data], axis=-1)
        return encoded_features

    @property
    def predict(self) -> dict:
        """
        Predicts the record price using features provided from input data.

        :return: float predicted record price
        """
        encoded_features = self.encode
        predicted_price = self.__model.predict(encoded_features)

        return {
            "response": "ok",
            "predicted_price": predicted_price[0]
        }


