import streamlit as st
from services.food_service import list_foods, log_food,today_food_items
from services.nutrition_service import today_nutrition
from services.health_service import calculate_bmi
from services.activity_service import save_activity,today_activity
from services.progress_service import weekly_progress
import pandas as pd
from services.weight_service import save_weight,weight_history
# ================= USER DASHBOARD =================
def user_dashboard(user):

    st.sidebar.title("💪 FitWise User")

    menu = st.sidebar.selectbox(
        "Menu",
        ["Dashboard", "Profile", "Log Food", "Activity", "Progress", "Logout"]
    )

    # ---------- DASHBOARD ----------
    if menu == "Dashboard":

        st.title(f"Welcome {user['name']} 👋")

        nutrition = today_nutrition(user["user_id"])

        calories_today = nutrition["calories"] or 0
        protein_today = nutrition["protein"] or 0
        fat_today = nutrition["fat"] or 0
        carbs_today = nutrition["carbs"] or 0
        fiber_today = nutrition["fiber"] or 0

        calorie_goal = user["daily_calorie_goal"]

        # CALORIES
        st.subheader("Calories")
        calorie_progress = calories_today / calorie_goal if calorie_goal else 0

        st.metric("Calories Today", f"{int(calories_today)} / {calorie_goal}")
        st.progress(min(calorie_progress, 1.0))

        st.divider()

        # MACROS
        st.subheader("Macros")

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"Protein: {round(protein_today,1)} g")
            st.progress(min(protein_today / 120, 1.0))

            st.write(f"Fat: {round(fat_today,1)} g")
            st.progress(min(fat_today / 70, 1.0))

        with col2:
            st.write(f"Carbs: {round(carbs_today,1)} g")
            st.progress(min(carbs_today / 250, 1.0))

            st.write(f"Fiber: {round(fiber_today,1)} g")
            st.progress(min(fiber_today / 30, 1.0))
        st.divider()
        st.subheader("Today's Logged Foods")

        foods_today = today_food_items(user["user_id"])

        if foods_today:
            st.table(foods_today)
        else:
            st.info("No food logged today")
        
        st.divider()
        st.subheader("Log Today's Weight")

        weight_today = st.number_input(
            "Enter current weight (kg)",
            30.0, 200.0,step=0.1,
            value=float(user["weight"])
        )

        if st.button("Save Weight"):
            save_weight(user["user_id"], weight_today)

            # update session value also
            st.session_state.user["weight"] = weight_today

            st.success("Weight saved successfully!")       
        st.divider()
        st.subheader("Daily Activity Progress")

        activity = today_activity(user["user_id"])

        steps_today = activity["steps"] if activity else 0
        water_today = activity["water"] if activity else 0
        sleep_today = activity["sleep"] if activity else 0

        col1, col2, col3 = st.columns(3)

        with col1:
            st.write(f"Steps: {steps_today} / {user['daily_steps_goal']}")
            st.progress(min(steps_today / user["daily_steps_goal"], 1.0))

        with col2:
            st.write(f"Water: {water_today} / {user['daily_water_goal']}")
            st.progress(min(water_today / user["daily_water_goal"], 1.0))

        with col3:
            st.write(f"Sleep: {sleep_today} / {user['daily_sleep_goal']}")
            st.progress(min(sleep_today / user["daily_sleep_goal"], 1.0))
            # ---------- PROFILE ----------
    elif menu == "Profile":
        profile_page(user)

    # ---------- LOG FOOD ----------
    elif menu == "Log Food":
        log_food_page(user)
    elif menu == "Activity":
        activity_page(user)
    elif menu == "Progress":
        progress_page(user)
    elif menu == "Logout":
        confirm_logout()


# ================= LOG FOOD PAGE =================
def log_food_page(user):

    st.title("🍽 Log Food")

    foods = list_foods()

    food_map = {f["food_name"]: f["food_id"] for f in foods}

    selected_food = st.selectbox(
        "Select Food (type to search)",
        list(food_map.keys())
    )

    quantity = st.number_input("Quantity (grams)", 0.5, step=0.5)

    if st.button("Add Food"):
        log_food(user["user_id"], food_map[selected_food], quantity)
        st.success("Food logged successfully!")


# ================= PROFILE PAGE =================
def profile_page(user):

    st.title("👤 User Profile")

    # BASIC INFO
    st.subheader("Basic Information")
    col1, col2 = st.columns(2)

    col1.write(f"Name: {user['name']}")
    col1.write(f"Email: {user['email']}")
    col1.write(f"Phone: {user['phone']}")

    col2.write(f"City: {user['city']}")
    col2.write(f"Age: {user['age']}")

    st.divider()

    # BODY DETAILS
    st.subheader("Body Details")
    col1, col2 = st.columns(2)

    col1.write(f"Height: {user['height']} cm")
    col1.write(f"Weight: {user['weight']} kg")

    col2.write(f"BMI: {calculate_bmi(user['weight'],user['height'])}")
    col2.write(f"Goal: {user['goal']}")

    st.divider()

    # GOAL DETAILS
    st.subheader("Goal Details")
    col1, col2 = st.columns(2)

    col1.write(f"Target Weight: {user['target_weight']} kg")
    col1.write(f"Goal Duration: {user['goal_months']} months")

    col2.write(f"Daily Calorie Goal: {user['daily_calorie_goal']}")

    st.divider()

    # DAILY GOALS
    st.subheader("Daily Goals")
    col1, col2, col3 = st.columns(3)

    col1.write(f"Water Goal: {user['daily_water_goal']} glasses")
    col2.write(f"Steps Goal: {user['daily_steps_goal']}")
    col3.write(f"Sleep Goal: {user['daily_sleep_goal']} hrs")

def activity_page(user):

    st.title("🏃 Daily Activity")

    steps = st.number_input("Steps", 0, 50000)
    water = st.number_input("Water (glasses)", 0, 20)
    sleep = st.number_input("Sleep (hours)", 0.0, 12.0)

    if st.button("Save Activity"):
        save_activity(user["user_id"], steps, water, sleep)
        st.success("Activity saved successfully!")

def progress_page(user):

    st.title("📈 Progress")
    
    st.subheader("Weight Progress")

    weight_data = weight_history(user["user_id"])

    if weight_data:
        df = pd.DataFrame(weight_data)
        df = df.sort_values("log_date")

        st.line_chart(df.set_index("log_date")["weight"])
    else:
        st.info("No weight data available")

    data = weekly_progress(user["user_id"])

    if not data:
        st.info("No progress data available")
        return

    df = pd.DataFrame(data)
    df = df.sort_values("log_date")

    st.subheader("Calories (Last 7 Days)")
    st.line_chart(df.set_index("log_date")["calories"])

    st.subheader("Steps (Last 7 Days)")
    st.line_chart(df.set_index("log_date")["steps"])

def confirm_logout():

    import streamlit as st

    st.warning("Are you sure you want to logout?")

    col1, col2 = st.columns(2)

    if col1.button("Yes, Logout"):
        st.session_state.logged_in = False
        st.session_state.role = None
        st.session_state.user = None
        st.rerun()

    if col2.button("Cancel"):
        st.rerun()
