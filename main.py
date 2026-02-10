import streamlit as st
from ui import user_dashboard, admin_dashboard
from services.user_service import login_user, signup_user


class FitWiseApp:

    def __init__(self):
        st.set_page_config(
            page_title="FitWise",
            page_icon="💪",
            layout="wide"
        )

        self.init_session()

    # ---------------------------
    # SESSION STATE INIT
    # ---------------------------
    def init_session(self):
        if "logged_in" not in st.session_state:
            st.session_state.logged_in = False
            st.session_state.role = None
            st.session_state.user = None



    # ---------------------------
    # LOGIN PAGE
    # ---------------------------
    def login_page(self):
        st.title("🔐 Login")

        role = st.radio("Select Role", ["User", "Admin"])
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            user = login_user(email, password)

            if user:
                st.session_state.logged_in = True
                st.session_state.role = role
                st.session_state.user = user
                st.rerun()
            else:
                st.error("Invalid credentials")


    # ---------------------------
    # SIGNUP PAGE
    # ---------------------------
    def signup_page(self):
        st.title("📝 Signup")

        with st.form("signup_form"):

            name = st.text_input("Name")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")

            phone = st.text_input("Phone")
            city = st.text_input("City")

            age = st.number_input("Age", 10, 100)
            height = st.number_input("Height (cm)", 100, 250)

            weight = st.number_input("Weight (kg)", 30.0, 200.0)

            diet = st.selectbox("Diet", ["Veg", "Non-Veg"])
            goal = st.selectbox("Goal", ["Weight Loss", "Maintenance", "Weight Gain"])

            target_weight = st.number_input("Target Weight (kg)", 30.0, 200.0)
            goal_months = st.number_input("Time to achieve goal (months)", 1, 24)

            st.subheader("Daily Goals")

            water_goal = st.number_input("Daily Water Goal (glasses)", 1, 20)
            steps_goal = st.number_input("Daily Steps Goal", 1000, 50000)
            sleep_goal = st.number_input("Daily Sleep Goal (hours)", 1, 12)
            submit = st.form_submit_button("Signup")
            cal_goal=((weight-target_weight)*7700)//(goal_months*30)
            
            
            if submit:

                if goal == "Weight Loss" and target_weight >= weight:
                    st.error("Target weight must be LESS than current weight for weight loss")
                    return

                if goal == "Weight Gain" and target_weight <= weight:
                    st.error("Target weight must be GREATER than current weight for weight gain")
                    return
                
                data = {
                    "name": name,
                    "email": email,
                    "password": password,
                    "phone": phone,
                    "city": city,
                    "age": age,
                    "height": height,
                    "weight": weight,
                    "diet": diet,
                    "goal": goal,
                    "target_weight": target_weight,
                    "goal_months": goal_months,
                    "water_goal": water_goal,
                    "steps_goal": steps_goal,
                    "sleep_goal": sleep_goal,
                    "cal_goal": cal_goal
                }

                user = signup_user(data)

                st.session_state.logged_in = True
                st.session_state.role = "User"
                st.session_state.user = user
                st.rerun()


    
    # ---------------------------
    # LOGOUT
    # ---------------------------
    def logout(self):
        st.session_state.logged_in = False
        st.session_state.role = None
        st.session_state.user = None
        st.rerun()

    # ---------------------------
    # ROUTER
    # ---------------------------
    def run(self):

        if not st.session_state.logged_in:

            tab1, tab2 = st.tabs(["Login", "Signup"])

            with tab1:
                self.login_page()

            with tab2:
                self.signup_page()

        else:
            if st.session_state.role == "User":
                user_dashboard.user_dashboard(st.session_state.user)
            else:
                admin_dashboard.admin_dashboard()


# ---------------------------
# START APP
# ---------------------------
app = FitWiseApp()
app.run()
