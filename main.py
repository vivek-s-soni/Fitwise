import streamlit as st
from ui import user_dashboard
from services.user_service import login_user, signup_user,email_exists


class FitWiseApp:

    def __init__(self):
        st.set_page_config(
            page_title="FitWise",
            page_icon="💪",
            layout="wide"
        )
        self.init_session()

    # ---------------------------
    # SESSION INIT
    # ---------------------------
    def init_session(self):
        if "logged_in" not in st.session_state:
            st.session_state.logged_in = False
        if "user" not in st.session_state:
            st.session_state.user = None

    # ---------------------------
    # PASSWORD VALIDATION
    # ---------------------------
    def is_strong_password(self, password):

        if len(password) < 8:
            return False, "Password must be at least 8 characters long"

        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False

        special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"

        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            elif char in special_chars:
                has_special = True

        if not has_upper:
            return False, "Password must contain at least 1 uppercase letter"
        if not has_lower:
            return False, "Password must contain at least 1 lowercase letter"
        if not has_digit:
            return False, "Password must contain at least 1 digit"
        if not has_special:
            return False, "Password must contain at least 1 special character"

        return True, ""

    # ---------------------------
    # LOGIN PAGE
    # ---------------------------
    def login_page(self):
        st.title("🔐 Login")

        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            user = login_user(email, password)

            if user:
                st.session_state.logged_in = True
                st.session_state.user = user
                st.rerun()
            else:
                st.error("Invalid email or password")

    # ---------------------------
    # SIGNUP PAGE
    # ---------------------------
    def signup_page(self):

        st.title("📝 Signup")

        with st.form("signup_form"):

            # Basic Info
            name = st.text_input("Name")
            email = st.text_input("Email")
            # -------- EMAIL UNIQUENESS CHECK --------
            if email_exists(email.strip()):
                st.error("An account with this email already exists")
                return
            password = st.text_input("Password", type="password")
            phone = st.text_input("Phone")
            city = st.text_input("City")

            # Body Info
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

            if submit:

                # -------- REQUIRED VALIDATION --------
                if not name.strip():
                    st.error("Name is required")
                    return

                if not city.strip():
                    st.error("City is required")
                    return

                # -------- EMAIL VALIDATION --------
                if "@" not in email or "." not in email:
                    st.error("Invalid email format")
                    return

                # -------- PHONE VALIDATION --------
                if not phone.isdigit() or len(phone) != 10:
                    st.error("Phone number must be exactly 10 digits")
                    return

                # -------- PASSWORD VALIDATION --------
                is_valid, message = self.is_strong_password(password)
                if not is_valid:
                    st.error(message)
                    return

                # -------- GOAL VALIDATION --------
                if goal == "Weight Loss" and target_weight >= weight:
                    st.error("Target weight must be LESS than current weight for weight loss")
                    return

                if goal == "Weight Gain" and target_weight <= weight:
                    st.error("Target weight must be GREATER than current weight for weight gain")
                    return

                # -------- CALORIE CALCULATION --------
                maintenance = weight * 30
                adjustment = abs(weight - target_weight) * 7700 / (goal_months * 30)

                if goal == "Weight Loss":
                    cal_goal = int(maintenance - adjustment)
                elif goal == "Weight Gain":
                    cal_goal = int(maintenance + adjustment)
                else:
                    cal_goal = int(maintenance)

                data = {
                    "name": name.strip(),
                    "email": email.strip(),
                    "password": password,
                    "phone": phone,
                    "city": city.strip(),
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

                st.success("Signup successful!")
                st.session_state.logged_in = True
                st.session_state.user = user
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
            user_dashboard.user_dashboard(st.session_state.user)


# ---------------------------
# START APP
# ---------------------------
app = FitWiseApp()
app.run()