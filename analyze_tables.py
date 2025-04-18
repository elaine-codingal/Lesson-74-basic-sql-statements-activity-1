# Import file from your system
file_path = "c:/Users/ELAINE_DEV/Documents/Lesson-74-SQLLite-Python-activity-acp/basketball.sqlite"
print("Selected file:", file_path)


"""### **2. Connect with SQLite Databases"""

# Connect with sqlite database
# Import necessary libraries
import sqlite3
import pandas as pd

database = 'database.sqlite'

conn = sqlite3.connect(database)
print('Opened data successfully')

#Query all tables in the database
tables = pd.read_sql("""
    SELECT name AS table_name
    FROM sqlite_master
    WHERE type='table';
""", conn)


#Read Table from the database into a dataframe
matches=pd.read_sql("""SELECT * FROM Match;""", conn)

#Print Table information
print(matches.info())