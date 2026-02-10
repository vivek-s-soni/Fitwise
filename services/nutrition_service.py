from dao.food_log_dao import get_today_nutrition
from datetime import date

def today_nutrition(user_id):
    return get_today_nutrition(user_id, date.today())
