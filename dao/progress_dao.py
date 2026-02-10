from db.connection import get_connection

def get_weekly_progress(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT log_date,
           SUM(calories) AS calories,
           SUM(steps) AS steps
    FROM (
        SELECT fl.log_date,
               (f.calories * fl.quantity) AS calories,
               0 AS steps
        FROM food_logs fl
        JOIN foods f ON fl.food_id = f.food_id
        WHERE fl.user_id = %s

        UNION ALL

        SELECT log_date,
               0 AS calories,
               steps
        FROM activity_logs
        WHERE user_id = %s
    ) x
    GROUP BY log_date
    ORDER BY log_date DESC
    LIMIT 7
    """

    cursor.execute(query, (user_id, user_id))
    result = cursor.fetchall()

    conn.close()
    return result
