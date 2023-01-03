import sqlite3
conn = sqlite3.connect('users.sqlite')
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS Users(
TG_ID INTEGER ,
Telefon INTEGER ,
Ism STRING,
Stage INTEGER
)
""")
first_insert = """
INSERT INTO Users VALUES ("{}" , " ", " ", "{}")
"""




get_id = """
SELECT TG_ID 
FROM Users
Where TG_ID = "{}"
"""

upd_Telefon = """
UPDATE Users 
SET Telefon = "{}" 
WHERE TG_ID = "{}"
"""
select_Telefon = """
SELECT Telefon 
From Users
WHERE TG_ID = "{}"
"""


upd_Ism = """
UPDATE Users 
SET Ism = "{}" 
WHERE TG_ID = "{}"
"""
select_Ism = """
SELECT Ism 
From Users
WHERE TG_ID = "{}"
"""


upd_Familiya = """
UPDATE Users 
SET Familiya = "{}" 
WHERE TG_ID = "{}"
"""
select_Familiya = """
SELECT Familiya 
From Users
WHERE TG_ID = "{}"
"""



upd_Stage = """
UPDATE Users 
SET Stage = "{}" 
WHERE TG_ID = "{}"
"""
select_Stage = """
SELECT Stage 
From Users
WHERE TG_ID = "{}"
"""
