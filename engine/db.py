import sqlite3
import csv

connection = sqlite3.connect("desijarvis.db")
cursor = sqlite3.Cursor(connection)

# querSYS = "CREATE TABLE IF NOT EXISTS sys_commands(id integer primary key, name varchar(100), path varchar(1000))"
# cursor.execute(querSYS)

# querSYS = "INSERT INTO sys_commands VALUES(null, 'vs code', 'C:\\Users\\Rajat Kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe')"
# cursor.execute(querSYS)

# querWEB = "CREATE TABLE IF NOT EXISTS web_commands(id integer primary key, name varchar(100), path varchar(1000))"
# cursor.execute(querWEB)

# querWEB = "INSERT INTO web_commands VALUES(null, 'canva', 'https://www.canva.com/en_in/')"
# cursor.execute(querWEB)

# queryContacts = "CREATE TABLE IF NOT EXISTS contact_info(id integer primary key, name varchar(100), contact varchar(13))"
# cursor.execute(queryContacts)

# with open('contacts.csv', 'r') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i].lower() for i in (0, 18)]
#         queryContacts = "INSERT INTO contact_info VALUES(null, ?, ?)"
#         cursor.execute(queryContacts, tuple(selected_data))


#cursor.execute("INSERT INTO contact_info VALUES(null, \"home\", 8968217951)")
#cursor.execute("DELETE FROM contact_info WHERE id = 10")
connection.commit()