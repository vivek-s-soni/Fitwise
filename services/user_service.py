from dao.user_dao import insert_user, get_user_by_email
from services.health_service import calculate_bmi, calorie_goal

def signup_user(data):
    insert_user(data)
    return get_user_by_email(data["email"])



def login_user(email, password):
    user = get_user_by_email(email)

    if user and user["password"] == password:
        return user

    return None
