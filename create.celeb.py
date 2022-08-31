# import sqlite3
import sqlite3

#check
print('sqlite imported successfully')

#create or connect to a database
conn = sqlite3.connect("Celeb.db")

#check the connection to a database
print(":connection created successfully!") ; print(type(conn))

# create a cursor object
c = conn.cursor()

#check
print(f'cursor created successfully! \n{type(c)}')

#create a database table:
c.execute(
    """
    CREATE TABLE celebrity(
        artist_name text,
        age INT,
        genre text,
        num_awards INT,
        num_albums INT,
        years_in_industry INT
        )
        """
)
print('celebrity table created successfully')

# # insert multiple 
celebrities = [("WIZKID", 32, "Afrobeats", 54, 7, 21),
                ("BURNA BOY", 31,  "dancehall", 22, 6, 12),
                ("DAVIDO", 29, "Afrobeats", 32, 6 ,13 ),
                ("OLAMIDE", 33, "hip hop", 21, 10, 13 ),
                ("TIWA SAVAGE", 42, "Afrobeats", 11, 4, 24),
                ("FALZ", 31, "Afropop", 6, 4, 13),
                ("PATORANKING", 32, "reggae", 12, 3, 13),
                ("SIMI", 34, "Afropop", 12, 4, 14),
                ("D'BANJ", 42, "Afrobeats", 17, 4, 18),
                ("2FACE", 46, "Afrobeats", 21, 5, 26),
                ("BANKY W", 41, "rap", 8, 4, 28),
                ("MI ABAGA", 40, "hip hop", 18, 4, 26),
                ("PSQUARE", 40, "Afropop", 17, 11, 27),
                ("YEMI ALADE", 33, "Afrobeats", 11, 5, 17),
                ("TEKNO", 29, "Afrobeats", 2, 1, 12),
                ("ASA", 39, "Afrobeats", 2, 6, 26),
                ("PHYNO", 35, "rap", 5,  5, 17),
                ("TIMAYA", 41, "Afrobeats", 7,  8, 17),
                ("ADEKUNLE GOLD", 35, "Afrobeats", 6,  4, 12),
                ("SINACH", 49, "rap", 5, 7, 27),
                ]


c.executemany("INSERT INTO celebrity VALUES(?, ?, ?, ? , ?, ?)", celebrities)

print('We have inserted', c.rowcount,' records to the table')

conn.commit()