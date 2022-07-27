# # import sqlite3
import sqlite3

# #check
print('sqlite imported successfully')

#create or connect to a database
conn = sqlite3.connect("SGA_1_3_learners.db")

#check the connection to a database
print(":connection created successfully!")

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
                ("Bukola", "Ajayi", "bukolaajayi@stutern.edu", "Data Science"),
                ("Christian", "Uzondu", "christianuzodu@stutern.edu", "Data Science"),
                ("Cynthia", "Awiya", "cynthiaaawiya@stutern.edu", "Data Science"),
                ("Eniola", "Osadare", "eniolaosadare@stutern.edu", "Data Science"),
                ("Esther", " Akpanowo", "estherakpanowo@stutern.edu", "Data Science"),
                ("Ganiyat", "Shittu", "ganiyatshittu@stutern.edu", "Data Science"),
                ("Jide", "Adesugba", "jideadesubga@stutern.edu", "Data Science"),
                ("Joyce", "Ezeonwu", "joyceezeonwu@stutern.edu", "Data Science"),
                ("Kafayat", "Ibrahim", "kafayatibrahim@stutern.edu", "Data Science"),
                ("Kehinde", "Orolade", "kehindeorolade@stutern.edu", "Data Science"),
                ("Lawrence", "Aneshimokha", "lawrenceaneshimokha@stutern.edu", "Data Science"),
                ("Mariam", "Adeoti", "mariamadeoti@stutern.edu", "Data Science"),
                ("Olorunnishola", "Olouwatosin", "olorunnisholaoluwatosin@stutern.edu", "Data Science"),
                ("Oluwaseyi", "Nicholas", "oluwaseyinicholas@stutern.edu", "Data Science"),
                ("Placidus", "Ali", "placidusali@stutern.edu", "Data Science"),
                ("Praise", "Emmanuel", "praiseemmanuel@stutern.edu", "Data Science"),
                ("Prince", "Ekeocha", "princeekeocha@stutern.edu", "Data Science"),
                ("Ramotallah", "Jubril", "ramotallahjubril@stutern.edu", "Data Science"),
                ("Rashidat", "Sikiru", "rashidatsikiru@stutern.edu", "Data Science"),
                ("Sheriff", "Olaitan", "sheriffolaitan@stutern.edu", "Data Science"),
                ("Stephen", "Ogunbile", "stephenogunbile@stutern.edu", "Data Science"),
                ("Temitope", "Bamidele", "temitopebamidele@stutern.edu", "Data Science"),
                ("Theresa", "Karamor", "theresakaramor@stutern.edu", "Data Science"),
                ("Tina", "Uyateide", "tinauyateide@stutern.edu", "Data Science"),
                ("Victoria", "Chukwuno", "victoriachukwuno@stutern.edu", "Data Science")
                ]

c.executemany("INSERT INTO SGA_1_3_learners VALUES(?, ?, ?, ? )", student_list)

print('We have inserted', c.rowcount,' records to the table')

# to Query my table in data base
c.execute("SELECT * FROM SGA_1_3_learners")

# to fetch my table 
items = c.fetchall()

#format output to display in tabular form
print("first_name"+ "\t surname"+ "\t\t\te-mail" "\t\t\t\t\t course \n" f'{"." *150}')

# loop through my items
for item in items:
    first_name, last_name, email, course = item
    print(f"{first_name:17}{last_name:31}{email:41}{course}")

# to commit my table
conn.commit()

# to close my database
conn.close()
