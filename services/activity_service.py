from dao.activity_dao import log_activity,get_today_activity

def save_activity(user_id, steps, water, sleep):
    log_activity(user_id, steps, water, sleep)

def today_activity(user_id):
    return get_today_activity(user_id)