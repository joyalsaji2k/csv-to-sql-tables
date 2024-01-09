import pandas as pd
from sqlalchemy import create_engine
import psycopg2 #used for postgres
conn_string='postgresql://postgres:123@localhost:5432/painting'
# postgresql://username:password@hostname:port/database_name
# Replace the placeholders with your PostgreSQL server details:

# username: Your PostgreSQL username
# password: Your PostgreSQL password
# hostname: The host where PostgreSQL is running (e.g., localhost, an IP address, or a domain)
# port: The port on which PostgreSQL is listening (default is usually 5432)
# database_name: The name of your PostgreSQL database
db=create_engine(conn_string)
conn=db.connect()
files =['artist', 'canvas_size','image_link','museum_hours','museum','product_size','subject','work']
# all the csv files are listed here under files

# data set fetching
for file in files:
    # used to fetch each files
    df=pd.read_csv(f'I:/zdumb/{file}.csv')
    # the f before a string literal denotes an f-string. F-strings allow for easy string
    # formatting by embedding expressions within curly braces {} inside the string.
    df.to_sql(file,con=conn,if_exists='replace',index=False)
