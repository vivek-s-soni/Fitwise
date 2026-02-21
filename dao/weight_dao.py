from db.connection import get_connection
from datetime import date

def log_weight(user_id, weight):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO weight_logs (user_id, weight, log_date)
    VALUES (%s,%s,%s)
    ON DUPLICATE KEY UPDATE
        weight = VALUES(weight)
    """

    cursor.execute(query, (user_id, weight, date.today()))
    conn.commit()
    conn.close()

def get_weight_history(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT log_date, AVG(weight) as weight
    FROM weight_logs
    WHERE user_id = %s
    GROUP BY log_date
    ORDER BY log_date DESC
    LIMIT 7
    """

    cursor.execute(query, (user_id,))
    data = cursor.fetchall()

    conn.close()
    return data