from classes.URI import URI
from classes.Exception import Exception
import sqlite3

class Database:

    def __init__(self, filename):
        self.__filename = filename + ".sqlite3"
        self.__createFile()

    def __createFile(self):
        try:
            connection = sqlite3.connect(self.__filename)
            self.__createTableURI(connection)
            self.__createTableException(connection)
        except sqlite3.Error:
            pass
        finally:
            if connection:
                connection.close()

    def __createTableURI(self, connection):
        cursor = connection.cursor()
        query = """
            CREATE TABLE if not exists "uri" (
                "ID"	INTEGER NOT NULL,
                "Name"	TEXT NOT NULL,
                "URI"	TEXT NOT NULL,
                "Selector"	TEXT NOT NULL,
                "Value"	TEXT NOT NULL,
                "Trash"	TEXT DEFAULT 0,
                PRIMARY KEY("ID" AUTOINCREMENT)
            );
        """
        cursor.execute(query)
        connection.commit()
        cursor.close()

    def __createTableException(self, connection):
        cursor = connection.cursor()
        query = """
            CREATE TABLE "exception" (
                "ID"	INTEGER NOT NULL,
                "Value"	TEXT NOT NULL,
                "Trash"	INTEGER DEFAULT 0,
                PRIMARY KEY("ID" AUTOINCREMENT)
            );
        """
        cursor.execute(query)
        connection.commit()
        cursor.close()

    def __getListURI(self, connection):
        cursor = connection.cursor()
        query = """
            select 
                "ID" as "id",
                "Name" as "name",
                "URI" as "uri",
                "Selector" as "selector",
                "Value" as "value",
                "Trash" as "trash"
            from 
                uri;
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def getListURI(self):
        list = []
        try:
            connection = sqlite3.connect(self.__filename)
            connection.row_factory = sqlite3.Row
            for item in self.__getListURI(connection):
                list.append(URI(item))
        except sqlite3.Error as error:
            print(error)
        finally:
            if connection:
                connection.close()
        return list

    def __getListException(self, connection):
        cursor = connection.cursor()
        query = """
            select 
                "ID" as "id",
                "Value" as "value",
                "Trash" as "trash"
            from 
                exception;
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def getListException(self, as_list=False):
        list = []
        try:
            connection = sqlite3.connect(self.__filename)
            connection.row_factory = sqlite3.Row
            for item in self.__getListException(connection):
                if as_list:
                    list.append(item["value"])
                else:
                    list.append(Exception(item))
        except sqlite3.Error as error:
            print(error)
        finally:
            if connection:
                connection.close()
        return list
