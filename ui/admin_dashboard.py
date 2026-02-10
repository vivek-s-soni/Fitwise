import streamlit as st

def admin_dashboard():
    st.sidebar.title("⚙ Admin Panel")

    menu = st.sidebar.selectbox(
        "Menu",
        ["Add Diet Plan", "Add Workout", "Users"]
    )

    st.title("Admin Dashboard")
