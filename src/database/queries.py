from src.database.database import Database


class Queries:
    def __init__(self):
        self.__database = Database()

    def create_tables(self):
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

