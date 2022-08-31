# # import sqlite3
import sqlite3

# #check
print('sqlite imported successfully')

#create or connect to a database
conn = sqlite3.connect("Students.db")

#check the connection to a database
print(":connection created successfully!")

conn.commit()

# create a cursor object
c = conn.cursor()

# #check
print(f'cursor created successfully!')

# # insert multiple 
student_list = [("Abubakar", "Adisa", "abubarkaradisa@stutern.edu", "Data Science"),
                ("Adedoyin", "Abass", "adedoyinabass@stutern.edu", "Data Science"),
                ("Ade", "Afolabi", "adeafolabi@stuteern.edu", "Data Science"),
                ("Amure", "Faith", "amurefaith@stutern.edu", "Data Science"),
                ("Angel", "Emmanuel", "angelaemmanuel@stutern.edu", "Data Science"),
                ("Awonaike", "Tawakalitu", "awonaiketawakalitu@stutern.edu", "Data Science"),
                ("Awoniran", "Omowunmi", "awoniranomowunmi@stutern.edu", "Data Science"),
                ("Binta", "Umar", "bintaumar@stutern.edu", "Data Science"),
                ("victoria", "Chukwuno", "victoriachukwuno@stutern.edu", "Data Science")
                ]

c.executemany("INSERT INTO SGA_1_3_learner VALUES(?, ?, ?, ? )", student_list)

print('We have inserted', c.rowcount,' records to the table')

#to alter the name of my table 
c.execute("""ALTER TABLE SGA_1_3_learner 
        RENAME TO DATA_science_learners;
        """)
print("we have renamed the table successfully")

c.execute("""ALTER TABLE DATA_science_learners 
         ADD COLUMN classes TEXT;
         """)
print("we have added a new column")

c.execute("""UPDATE DATA_science_learners
        SET classes = "2"
        WHERE first_name ='Binta';

""")


# to Query my table in data base
c.execute("SELECT * FROM DATA_science_learners")

# to fetch my table 
items = c.fetchall()

# print(items)

#format output to display in tabular form
print("first_name"+ "\t surname"+ "\t\t\te-mail" "\t\t\t\t\t course" + "\t\t\t classes  \n" f'{"." *150}')

# loop through my items
for item in items:
    first_name, surname, email, course, classes = item
    print(f"{first_name:17}{surname:31}{email:41}{course:25}{classes}")

# to commit my table
conn.commit()

# to close my database
conn.close()