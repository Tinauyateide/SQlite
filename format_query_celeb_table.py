# # import sqlite3
import sqlite3

# #check
print('sqlite imported successfully')

#create or connect to a database
conn = sqlite3.connect("Celeb.db")

#check the connection to a database
print(":connection created successfully!")

conn.commit()

# create a cursor object
c = conn.cursor()

# #check
print(f'cursor created successfully!')

# to query my table to print most decorated artist 
c.execute("""SELECT * FROM celebrity
        ORDER BY num_awards DESC
        LIMIT 1;
""")
most_decorated = c.fetchall()
print(most_decorated)

# to query my table to print the oldest celebrity
c.execute("""SELECT * FROM celebrity WHERE age = 
(SELECT MAX(age) FROM celebrity);
""")
oldest = c.fetchall()
print(oldest)

# query my table to print who has been in the industry the longest
c.execute("""SELECT * FROM celebrity WHERE  years_in_industry= 
(SELECT MAX(years_in_industry) FROM celebrity);
""")
longest_industry = c.fetchall()
print(longest_industry)

#query my table to print least number of albums
c.execute("""SELECT * FROM celebrity WHERE  num_albums= 
(SELECT MIN(num_albums) FROM celebrity);
""")

least_albums = c.fetchall()
print(least_albums)

# query my album to pick most popular genre of music
c.execute("""SELECT genre
        FROM celebrity
        GROUP BY genre
        ORDER BY COUNT(*) DESC
        LIMIT 1;""")

popular_genre = c.fetchall()
print(popular_genre)