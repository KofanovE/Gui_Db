## IMPORTS

import os
import sys

# Import SQLite
import sqlite3
from sqlite3 import Error

# Import QtableWidgetItem (for creating new table cells)
from PySide2.QtWidgets import QTableWidgetItem


# Function class
class AppFunctions():

    """docstring for AppFunctions"""

    def __init__(self, arg):
        super(AppFunctions, self).__init__()
        self.arg = arg


    ## Create database connection
    def create_connection(db_file):

        """ create a database connection to a SQLite database"""
        
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        # Return connection
        return conn

    ## Create table
    def create_table(conn, create_table_sql):
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)


    ## Main function
    def main(dbFolder):
        # Create table if it does not exist
        create_user_table = """ CREATE TABLE IF NOT EXISTS Users (
                                    USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                    USER_NAME TEXT,
                                    USER_EMAIL TEXT,
                                    USER_PHONE TEXT
                                );
                            """
        conn = AppFunctions.create_connection(dbFolder)

        # create tables
        if conn is not None:
            # create user table
            AppFunctions.create_table(conn, create_user_table)
        else:
            print('Error! Cannot create the database connection')


    ## Get all users from database
    def getAllUsers(dbFolder):
        # create db connection
        conn = AppFunctions.create_connection(dbFolder)

        get_all_users = """
                            SELECT * FROM Users;
                        """
        try:
            c = conn.cursor()
            c.execute(get_all_users)
            # return all table rows
            return c
        except Error as e:
            print(e)

    ## Add a user to db
    def addUser(self, dbFolder):
        # create db connection
        conn = AppFunctions.create_connection(dbFolder)
        # get form values
        userName = self.ui.userName.text()
        email = self.ui.email.text()
        phoneNo = self.ui.phoneNo.text()

        # create sql statement
        insert_person_data_sql = f"""
        INSERT INTO Users (USER_NAME, USER_EMAIL, USER_PHONE) VALUES ('{userName}',
                '{email}', '{phoneNo}');
        """

        # execute sql statement
        if not conn.cursor().execute(insert_person_data_sql):
            print("Could not insert person data")
        else:
            conn.commit()
            # clear form input
            self.ui.userName.setText("")
            self.ui.email.setText("")
            self.ui.phoneNo.setText("")
            # load new user from DB to table view
            AppFunctions.displayUsers(self, AppFunctions.getAllUsers(dbFolder))

        
    ## Display users
    def displayUsers(self, rows):
        # loop through all rows
        for row in rows:
            # get number of rows
            rowPosition = self.ui.tableWidget.rowCount()

            # skip rows that have alreade been loaded to table
            if rowPosition + 1 > row[0]:
                continue
            
            itemCount = 0
            # create new table row
            self.ui.tableWidget.setRowCount(rowPosition+1)
            qtablewidgetitem = QTableWidgetItem()
            self.ui.tableWidget.setVerticalHeaderItem(rowPosition, qtablewidgetitem)

            # add items to row
            for item in row:
                self.qtablewidgetitem = QTableWidgetItem()
                self.ui.tableWidget.setItem(rowPosition, itemCount, self.qtablewidgetitem)
                self.qtablewidgetitem = self.ui.tableWidget.item(rowPosition, itemCount)
                self.qtablewidgetitem.setText(str(item))

                itemCount = itemCount + 1
            rowPosition = rowPosition + 1

                
            
        
    
