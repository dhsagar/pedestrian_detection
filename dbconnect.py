import mysql.connector as mdc
#connecting to database
mydb = mdc.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    port = '3306',
    database = 'pedestrian'
)

