from dao.food_dao import get_all_foods
from dao.food_log_dao import add_food_log,get_today_food_logs
from datetime import date

def list_foods():
    return get_all_foods()

def log_food(user_id, food_id, quantity):
    today = date.today()
    add_food_log(user_id, food_id, quantity, today)

def today_food_items(user_id):
    return get_today_food_logs(user_id, date.today())
