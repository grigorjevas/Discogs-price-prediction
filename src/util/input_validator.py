class InputValidator:
    def __init__(self, input_data):
        self.__input_data = input_data

    @property
    def validate_keys(self) -> dict:
        valid_keys = ("artist", "title", "release_format", "number_of_tracks", "release_year", "rating",
                      "votes", "have", "want", "limited_edition", "media_condition", "sleeve_condition")
        if not all(name in self.__input_data for name in valid_keys):
            return {
                "response": "error",
                "validation_errors": "missing keys, please refer to documentation"
            }
        return {"response": "ok"}

    @property
    def validate_input(self) -> [list, bool]:
        validation_errors = []
        if self.validate_artist_not_str:
            validation_errors.append(self.validate_artist_not_str)
        if self.validate_title_not_str:
            validation_errors.append(self.validate_title_not_str)
        if self.validate_release_format_not_str:
            validation_errors.append(self.validate_release_format_not_str)
        if self.validate_artist_name_empty:
            validation_errors.append(self.validate_artist_name_empty)
        if self.validate_title_empty:
            validation_errors.append(self.validate_title_empty)
        if self.validate_release_format_empty:
            validation_errors.append(self.validate_release_format_empty)
        if self.validate_release_format_categories:
            validation_errors.append(self.validate_release_format_categories)
        if self.validate_limited_edition:
            validation_errors.append(self.validate_limited_edition)
        if self.validate_numbers:
            validation_errors.append(self.validate_numbers[0])

        if validation_errors:
            return {
                "response": "error",
                "validation_errors": validation_errors
            }
        return {"response": "ok"}

    @property
    def validate_artist_not_str(self) -> [str, None]:
        if not isinstance(self.__input_data["artist"], str):
            return "Invalid data type for artist supplied. Artist name must be a string."
        return

    @property
    def validate_title_not_str(self) -> [str, None]:
        if not isinstance(self.__input_data["title"], str):
            return "Invalid data type for title supplied. Title must be a string."

    @property
    def validate_release_format_not_str(self) -> [str, None]:
        if not isinstance(self.__input_data["release_format"], str):
            return "Invalid data type for release format. Release format must be a string."

    @property
    def validate_artist_name_empty(self) -> [str, None]:
        if not self.__input_data["artist"]:
            return "Artist name cannot be empty."

    @property
    def validate_title_empty(self) -> [str, None]:
        if not self.__input_data["title"]:
            return "Title cannot be empty."

    @property
    def validate_release_format_empty(self) -> [str, None]:
        if not self.__input_data["release_format"]:
            return "Release format cannot be empty."

    @property
    def validate_release_format_categories(self) -> [str, None]:
        available_categories = ['12"', '10"', '7"', 'LP', 'EP']
        if self.__input_data["release_format"] not in available_categories:
            return f"Unknown release format category. Available categories: {available_categories}"

    @property
    def validate_limited_edition(self) -> [str, None]:
        if not isinstance(self.__input_data["limited_edition"], bool):
            return "Invalid data type for limited edition. Limited edition must be a boolean (true/false)."

    @property
    def validate_numbers(self) -> list:
        numerical_variables = [
            self.__input_data["number_of_tracks"],
            self.__input_data["release_year"],
            self.__input_data["rating"],
            self.__input_data["votes"],
            self.__input_data["have"],
            self.__input_data["want"],
            self.__input_data["media_condition"],
            self.__input_data["sleeve_condition"]
        ]
        errors = []
        for val in numerical_variables:
            if not isinstance(val, (int, float)):
                errors.append(f"Invalid data type {val}. Please provide a numeric value.")
        return errors
