from db.connection import get_connection

def get_all_foods():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM foods")
    foods = cursor.fetchall()

    conn.close()
    return foods
