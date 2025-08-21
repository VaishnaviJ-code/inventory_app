import configparser
import mysql.connector
from mysql.connector import Error


class DBConnection:

    '''
        establlish a singleton connection with db
        this class will create only one instance
    '''

    __instance = None # to store the singleton instance

    def __new__(cls): # this is a class method - it (class methods and class variable) loads when the class is loaded i.e., before the constructor is loaded

        '''
            override to implement singleton
            ensures only one instane of DBConnection id ever created
        '''

        if cls.__instance is None: # if no instance created
            cls.__instance = super(DBConnection, cls).__new__(cls)
            cls.__instance.__initialize() # initialize the connection once

        return cls.__instance # return the same instance
    
    def __initialize(self):

        '''
            initialize the database connection using properties
            from the db_config.ini
        '''

        try:

            # load the configuration file 
            config = configparser.ConfigParser()
            config.read("db_config.ini") # this is a file that has all the properties required for the connection to MySQL

            #extablish the MySQL connection
            self.connection = mysql.connector.connect(
                host = config.get("mysql", "host"),
                user = config.get("mysql", "user"),
                password = config.get("mysql", "password"),
                database = config.get("mysql", "database")
            )

            if self.connection.is_connected():
                print("Connecting to MySQL database...")

        except Error as e:

            print(f"Error while connection to MySQL: {e}")
            self.connection = None
    
    def get_connection(self):
        return self.connection