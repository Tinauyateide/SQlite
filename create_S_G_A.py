# import sqlite3
import sqlite3

#check
print('sqlite imported successfully')

#create or connect to a database
conn = sqlite3.connect("SGA_1_3_learners.db")

#check the connection to a database
print(":connection created successfully!") ; print(type(conn))

# create a cursor object
c = conn.cursor()

#check
print(f'cursor created successfully! \n{type(c)}')

# #create a database table:
c.execute(
    """
    CREATE TABLE SGA_Students(
        first_name text,
        last_name text,
        email_address text,
        course text
        )
        """
)
print('students table created successfully')