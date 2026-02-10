from dao.weight_dao import log_weight,get_weight_history

def save_weight(user_id, weight):
    log_weight(user_id, weight)


def weight_history(user_id):
    return get_weight_history(user_id)
