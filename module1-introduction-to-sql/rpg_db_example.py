import sqlite3

def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

GET_CHARACTERS = """
  SELECT *
  FROM charactercreator_character;
"""
#1
SELECT * FROM charactercreator_character;
SELECT COUNT(*) FROM charactercreator_character;
SELECT COUNT(name) FROM charactercreator_character;

#2

#5
SELECT character_id, COUNT(DISTINCT item_id) FROM
(SELECT cc.character_id, cc.name AS character_name, ai.item_id, ai.name AS item_name, aw.item_ptr_id AS weapon_name
FROM charactercreator_character AS cc,
armory_item AS ai,
charactercreator_character_inventory AS cci,
armory_weapon As aw
WHERE cc.character_id = cci.character_id
AND ai.item_id = cci.item_id
And ai.item_id = aw.item_ptr_id)
GROUP BY 1 ORDER BY 2 DESC
LIMIT 20;

#6
SELECT character_id, COUNT(DISTINCT weapon_name) FROM
(SELECT cc.character_id, cc.name AS character_name, ai.item_id, ai.name AS item_name, aw.item_ptr_id AS weapon_name
FROM charactercreator_character AS cc,
armory_item AS ai,
charactercreator_character_inventory AS cci,
armory_weapon As aw
WHERE cc.character_id = cci.character_id
AND ai.item_id = cci.item_id
And ai.item_id = aw.item_ptr_id)
GROUP BY 1 ORDER BY 2 DESC
LIMIT 20;

if __name__ == '__main__':
    conn = connect_to_db()
    curs = conn.cursor()
    results = execute_query(curs, GET_CHARACTERS)
    print(results)