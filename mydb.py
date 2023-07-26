import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
database = mysql.connector.connect(
    host=os.environ.get('DB_HOST'),
    user=os.environ.get('DB_USER'),
    passwd=os.environ.get('DB_PASS')
)

cursor_object = database.cursor()

cursor_object.execute("CREATE DATABASE joaocompany")

print("All Done!")
