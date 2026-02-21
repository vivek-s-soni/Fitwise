from db.connection import get_connection


def add_food_log(user_id, food_id, quantity, date,meal):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO food_logs (user_id, food_id, quantity, log_date,meal_type)
    VALUES (%s,%s,%s,%s,%s)
    """

    cursor.execute(query, (user_id, food_id, quantity, date,meal))
    conn.commit()
    conn.close()

def get_daily_nutrition(user_id, date):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT
        SUM(f.calories * fl.quantity) AS total_calories,
        SUM(f.protein * fl.quantity) AS total_protein,
        SUM(f.carbs * fl.quantity) AS total_carbs,
        SUM(f.fat * fl.quantity) AS total_fat,
        SUM(f.fiber * fl.quantity) AS total_fiber
    FROM food_logs fl
    JOIN foods f ON fl.food_id = f.food_id
    WHERE fl.user_id = %s AND fl.log_date = %s
    """

    cursor.execute(query, (user_id, date))
    result = cursor.fetchone()
    conn.close()

    return result

def get_today_nutrition(user_id, date):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT
        SUM(f.calories * fl.quantity) AS calories,
        SUM(f.protein * fl.quantity) AS protein,
        SUM(f.carbs * fl.quantity) AS carbs,
        SUM(f.fat * fl.quantity) AS fat,
        SUM(f.fiber * fl.quantity) AS fiber
    FROM food_logs fl
    JOIN foods f ON fl.food_id = f.food_id
    WHERE fl.user_id = %s AND fl.log_date = %s
    """

    cursor.execute(query, (user_id, date))
    result = cursor.fetchone()

    conn.close()
    return result

def get_today_food_logs(user_id, date):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT fl.food_log_id,
            f.food_name,
            fl.quantity,
            fl.meal_type,
            (f.calories * fl.quantity) AS calories
        FROM food_logs fl
        JOIN foods f ON fl.food_id = f.food_id
        WHERE fl.user_id = %s AND fl.log_date = %s
        """

    cursor.execute(query, (user_id, date))
    result = cursor.fetchall()

    conn.close()
    return result
def get_today_food_logs(user_id, date):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT fl.log_id,
        f.food_name,
        fl.quantity,
        fl.meal_type,
        (f.calories * fl.quantity) AS calories
    FROM food_logs fl
    JOIN foods f ON fl.food_id = f.food_id
    WHERE fl.user_id = %s AND fl.log_date = %s
    """

    cursor.execute(query, (user_id, date))
    result = cursor.fetchall()

    conn.close()
    return result

def delete_food_log(log_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM food_logs WHERE log_id=%s"
    cursor.execute(query, (log_id,))

    conn.commit()
    conn.close()
    
def update_food_log(log_id, new_quantity):
    conn = get_connection()
    cursor = conn.cursor()

    query = "UPDATE food_logs SET quantity=%s WHERE log_id=%s"
    cursor.execute(query, (new_quantity, log_id))

    conn.commit()
    conn.close()