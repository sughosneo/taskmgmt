'''

    This manager script would actually be responsible to process individual task from rabbitmq
    It would do following -
        - Inherits basic Task operation from Celery Task library.
        - Performs processing each email.
        - Inserts each processed message into MySQL.
'''

from celery import Task

from ProcessingMgr import *
from MySQLDBHelper import *

class TaskMgr(Task):

    __EMAIL_CSV_FILE_PATH = "/taskmgmt/data/emails.csv"

    @app.task(base=TaskMgr, queue="parse")
    def parse(self):

        print("[Info]: Inside in TaskMgr.parse()")

        try:

            processingMgr = ProcessingMgr()
            processingMgr.loadEmailCSV(self.__EMAIL_CSV_FILE_PATH)

        except Exception as error:
            print("[Error]: ", str(error))

    @app.task(base=TaskMgr, queue="insertValue", ignore_result=True)
    def insertValue(self):

        print("[Info]: Inside in TaskMgr.insertValue()")

        try:

            mySQLDBHelper = MySQLDBHelper()
            mySQLDBHelper.insert()

        except Exception as error:
            print("[Error]: ", str(error))




