from src.database.database import Database


class Queries:
    def __init__(self):
        self.__database = Database()

    def create_tables(self) -> None:
        """
        Builds table structure if it doesn't exist.

        :return: None
        """
        self.__database.execute_query('''
        CREATE TABLE IF NOT EXISTS history (
            id serial PRIMARY KEY,
            artist varchar(255),
            title varchar(255),
            release_format varchar(255),
            number_of_tracks INT,
            release_year INT,
            rating FLOAT,
            votes INT,
            have INT,
            want INT,
            limited_edition BOOL,
            media_condition INT,
            sleeve_condition INT,
            predicted_price FLOAT
        ); ''')

    def log_prediction(self, input_data, response) -> None:
        """
        Writes the request and prediction data to a database.

        :param input_data: validated json
        :param response: item price prediction json
        :return: None
        """
        query = f'''
            INSERT INTO history(
                artist, title, release_format, number_of_tracks, release_year, rating,
                votes, have, want, limited_edition, media_condition, sleeve_condition, 
                predicted_price) 
                VALUES('{input_data["artist"]}', '{input_data["title"]}', '{input_data["release_format"]}',
                '{input_data["number_of_tracks"]}', '{input_data["release_year"]}',' {input_data["rating"]}', 
                '{input_data["votes"]}', '{input_data["have"]}', '{input_data["want"]}', 
                '{input_data["limited_edition"]}', '{input_data["media_condition"]}', 
                '{input_data["sleeve_condition"]}', '{response["predicted_price"]}'); '''
        self.__database.execute_query(query)

    def get_predictions(self, predictions_to_show: int = 10) -> list:
        """
        Gets a specified number of predictions from the database.

        :param predictions_to_show:
        :return: list
        """
        return self.__database.execute_query_and_fetch(f'''
            SELECT * FROM history ORDER BY id DESC LIMIT {predictions_to_show}''')
