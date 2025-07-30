import os
from . import MySQLtoSQLite

class Main:
    def __init__(self):
        self.path = "../../Assets/StreamingAssets/Reference_Data.db"

        os.remove(self.path)

        converter = MySQLtoSQLite(
            sqlite_file=self.path,
            mysql_user="developer",
            mysql_password="idlerpg20250706!",
            mysql_database="reference_data",
            mysql_host="221.141.233.231",
            mysql_port=3306,
        )

        converter.transfer()
    
if __name__ == "__main__":
    Main()