import pymongo
import sqlite3

# Our objective was to transfer all the Characters from
# Charactor_creator in our SQl file to our MongoDB database


# first we must connect to our mongDB account
password = 'REDACTED'
dbname = 'test'
connection = ('mongodb+srv://ladksfnvlknjd:' + password +
              '@cluster0.ogvpk.mongodb.net/' + dbname +
              '?retryWrites=true&w=majority')
client = pymongo.MongoClient(connection)
db = client.test

# now we get our sql file and change its name
!wget https://github.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module1-introduction-to-sql/rpg_db.sqlite3?raw=true
!mv 'rpg_db.sqlite3?raw=true' rpg_db.sqlite3

# Construct our conn and our curs to extract characters
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# Now using curse we use SQL to extract the information
get_characters = 'SELECT * FROM charactercreator_character;'
characters = curs.execute(get_characters).fetchall()

# Using this for loop we transorm and load our data to MongDB
for char in characters:
    get_rpg_characters = {'Character_id': char[0],
                          'name': char[1],
                          'level': char[2],
                          'exp':  char[3],
                          'hp':  char[4],
                          'strength':  char[5],
                          'intelligence':  char[6],
                          'dexterity':  char[7],
                          'wisdom':  char[8]}
    db.test.insert_one(get_rpg_characters)

# Invoke db.test.find_one() to test our work
print(db.test.find_one({'name': 'Iure h'}))
