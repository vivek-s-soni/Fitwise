def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return round(weight / (height_m ** 2), 2)


def calorie_goal(weight, goal, activity_level="moderate"):
    # simple formula (can improve later)

    base = weight * 30

    if goal == "Weight Loss":
        base -= 500
    elif goal == "Weight Gain":
        base += 500

    return int(base)
def macro_goals(calories):

    protein = (calories * 0.30) / 4
    carbs   = (calories * 0.40) / 4
    fat     = (calories * 0.30) / 9
    fiber   = (calories / 1000) * 14

    return {
        "protein": round(protein, 1),
        "carbs": round(carbs, 1),
        "fat": round(fat, 1),
        "fiber": round(fiber, 1)
    }
