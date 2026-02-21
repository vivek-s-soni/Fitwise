from db.connection import get_connection
from services.health_service import macro_goals

def insert_user(data):

    conn = get_connection()
    cursor = conn.cursor()

    # ---- CALCULATE MACROS FIRST ----
    macros = macro_goals(data["cal_goal"])

    query = """
    INSERT INTO users
    (name,email,password,phone,city,age,height,weight,diet_type,goal,
    target_weight,goal_months,daily_water_goal,daily_steps_goal,
    daily_sleep_goal,daily_calorie_goal,
    daily_protein_goal,daily_carbs_goal,daily_fat_goal,daily_fiber_goal)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(query, (
        data["name"],
        data["email"],
        data["password"],
        data["phone"],
        data["city"],
        data["age"],
        data["height"],
        data["weight"],
        data["diet"],
        data["goal"],
        data["target_weight"],
        data["goal_months"],
        data["water_goal"],
        data["steps_goal"],
        data["sleep_goal"],
        data["cal_goal"],
        macros["protein"],
        macros["carbs"],
        macros["fat"],
        macros["fiber"]
    ))

    conn.commit()
    conn.close()

    return True

def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM users WHERE email=%s"
    cursor.execute(query, (email,))

    user = cursor.fetchone()
    conn.close()

    return user
def login_user(email, password):
    user = get_user_by_email(email)

    if user and user["password"] == password:
        return user
    return None
def fetch_all_users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT user_id, name, email, goal FROM users")
    users = cursor.fetchall()

    conn.close()
    return users
