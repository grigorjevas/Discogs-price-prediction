from dotenv import load_dotenv
import os
from psycopg2 import connect, OperationalError
load_dotenv()


class Database:
    def __init__(self):
        """
        Database class.

        Available methods:
            * connect
            * execute_query
            * execute_query_and_fetch
        """
        self.__database_url = os.environ["DATABASE_URL"]

    def connect(self):
        """
        Creates a new database connection. Reads the credentials from .env file.

        Returns postgreSQL database session and a new instance of connection class.
        By using the connection object you can create a new cursor to execute any SQL statements.

        Returns error if connection is unsuccessful.
        """
        try:
            connection = connect(self.__database_url)
            return connection
        except OperationalError as err:
            print("pg error: ", err.pgerror, "\n")
            print("pg code: ", err.pgcode, "\n")
            raise err

    def execute_query(self, query: str) -> None:
        """
        Executes SQL query. To be used for queries which do not return any results, for example:
        INSERT, UPDATE, CREATE, ALTER, DROP, etc.

        :param query: SQL query
        """
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()

    def execute_query_and_fetch(self, query: str) -> list:
        """
        Executes SQL query and fetches a response. To be used for queries whihc return results, for example: SELECT.

        :param query: SQL query
        :return: array
        """
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        return result
