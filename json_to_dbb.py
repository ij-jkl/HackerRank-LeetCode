#Script to convert JSON files to DBB format

import json
import mysql.connector

with open('ciudades-argentinas.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)


connection = mysql.connector.connect(
    host='',
    user='',
    password='',
    database=''
)
cursor = connection.cursor()

for provincia in json_data:
    provincia_id = provincia["id"]
    provincia_nombre = provincia["nombre"]

    cursor.execute("""
        INSERT IGNORE INTO Provinces (id, nombre)
        VALUES (%s, %s)
    """, (provincia_id, provincia_nombre))

    for ciudad in provincia["ciudades"]:
        ciudad_id = int(ciudad["id"])
        ciudad_nombre = ciudad["nombre"]

        cursor.execute("""
            INSERT IGNORE INTO Cities (id, nombre, provinceid)
            VALUES (%s, %s, %s)
        """, (ciudad_id, ciudad_nombre, provincia_id))

connection.commit()
cursor.close()
connection.close()

print("Data inserted successfully!")