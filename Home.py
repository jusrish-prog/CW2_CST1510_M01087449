import streamlit as st
from hashing import generate_hash, is_valid_hash
from app_model.database import get_connection
from app_model.users import add_user, get_user

connection = get_connection()

st.set_page_config("Home",layout= "wide")

st.title("Welcome to system home page")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "username" in st.session_state:
    login_username = st.session_state["username"]


tab_login, tab_register = st.tabs(["Login", "Register"])
with tab_login:
    login_username = st.text_input("Username")
    login_password = st.text_input("Password", type="password")


    if st.button("Log in"):
        id, user_name, user_hash, user_role = get_user(connection,login_username)
        if login_username == user_name and is_valid_hash(login_password,user_hash):
            st.session_state["logged_in"] = True
            st.session_state["username"] = login_username
            st.success("Logged in successfully!")
            st.switch_page("pages/Dashboard.py")

        elif len(login_username) == 0:
            st.warning("Please enter your username")
    
        elif login_username != user_name:
            st.warning("Wrong username entered.Please try again")

        elif len(login_password) == 0:
            st.warning("Please enter valid password")
        
        elif login_password != user_hash:
            st.warning("Wrong password entered.Please try again.")

        else:
            st.warning("Please enter correct password")

        st.session_state["logged_in"] = False
        

with tab_register:
    register_username = st.text_input("New username")

    special_characters = {"!","@","#","$","%","^"}
    found_lower = False
    found_upper = False
    found_digit = False
    found_special = False

    if len(register_username) == 0:
        st.warning("Please enter a username")

    elif len(register_username) <= 4:
        st.warning("Try creating a longer username.")

    for char in register_username:
        if char.islower() == True:
            found_lower = True
        if char.isupper() == True:
            found_upper = True
        if char.isdigit() == True:
            found_digit = True
        if char in special_characters:
            found_special = True

    if found_lower == False:
        st.warning("username must contain at least 1 lowercase letter.")
    
    if found_upper == False:
        st.warning("username must contain at least 1 uppercase letter.")

    if found_digit == False:
        st.warning("username must contain at least 1 digit.")
    
    if found_special == False:
        st.warning("username must contain at least 1 special character.")

    if found_lower and found_upper and found_digit and found_special == True:
        st.info("username meets requirements.")
    
    register_password = st.text_input("New password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    register_role = st.selectbox("Role",["admin", "user"])

    # if len(register_password) == 0:
    #     st.warning("Please register valid password")
    
    # elif len(register_password) > 0 and len(register_password) <= 4:
    #     st.warning("Password strength is weak.")
    #     st.info("Tip: Try entering a longer password(at least 5 characters)")

    # elif len(register_password) >= 5 and len(register_password) <= 8:
    #     st.info("Password strength is medium.")

    # elif len(register_password) > 8:
    #     st.info("Password strength is strong.")

    # elif len(confirm_password) == 0:
    #     st.warning("Please confirm password.")

    # elif confirm_password != register_password:
    #     st.warning("Password does not match!")

    if st.button("Register"):
        st.session_state["logged_in"] = False 
        hash_password = generate_hash(register_password)
        add_user(connection,register_username,hash_password,register_role)

        st.success("Registration is successfull.Please login next.")

st.session_state