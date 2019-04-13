'''
    This script would be responsible to handle all MySQL DB related operations.
'''

from sqlalchemy import *

class MySQLDBHelper:

    __messages_table = None

    def __init__(self):

        metadata = self.__createDatabase()
        self.__messages_table = self.__createTable()

    """Create DB and Table in the MySQL database"""
    def __createDatabase(self):

        print("[Info] - inside __createTable()")

        try:

            db = create_engine('mysql://root@localhost/taskmgmt')
            metadata = MetaData(db)

            return metadata

        except Exception as error:
            print("[Error]",str(error))

    def __createTable(self,metadata):

        print("[Info] - inside __createTable()")
        try:

            messages_table = Table('messages', metadata,
                                   Column('message_id', String(255), primary_key=True),
                                   Column('subject', String(255)),
                                   Column('to', String(255)),
                                   Column('x_to', String(255)),
                                   Column('from', String(255)),
                                   Column('x_from', String(255)),
                                   Column('cc', String(255)),
                                   Column('x_cc', String(255)),
                                   Column('bcc', String(255)),
                                   Column('x_bcc', String(255)),
                                   Column('payload', Text()))

            messages_table.create(checkfirst=True)

            return messages_table

        except Exception as error:
            print("[Error]", str(error))

    """Insert a message into the MySQL database"""
    def insert(self, message_dict):

        print("[Info] - inside insert()")

        if self.__messages_table is None:
            ins = self.__messages_table.insert(values=message_dict)
            ins.execute()