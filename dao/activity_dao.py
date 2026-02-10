from db.connection import get_connection
from datetime import date

def log_activity(user_id, steps, water, sleep):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO activity_logs (user_id, steps, water, sleep, log_date)
    VALUES (%s,%s,%s,%s,%s)
    ON DUPLICATE KEY UPDATE
        steps = steps + VALUES(steps),
        water = water + VALUES(water),
        sleep = VALUES(sleep)
    """

    cursor.execute(query, (user_id, steps, water, sleep, date.today()))
    conn.commit()
    conn.close()

def get_today_activity(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT steps, water, sleep
    FROM activity_logs
    WHERE user_id=%s AND log_date=%s
    """

    cursor.execute(query, (user_id, date.today()))
    result = cursor.fetchone()

    conn.close()
    return result
