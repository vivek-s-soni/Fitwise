from dao.food_dao import get_all_foods
from dao.food_log_dao import add_food_log,get_today_food_logs,delete_food_log,update_food_log
from datetime import date


def list_foods():
    return get_all_foods()

def log_food(user_id, food_id, quantity,meal):
    today = date.today()
    add_food_log(user_id, food_id, quantity, today,meal)
    
def remove_food_log(log_id):
    delete_food_log(log_id)
    
def today_food_items(user_id):
    return get_today_food_logs(user_id, date.today())

def edit_food_log(food_log_id, new_quantity):
    update_food_log(food_log_id, new_quantity)