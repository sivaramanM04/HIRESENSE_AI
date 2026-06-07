import streamlit as st


# ==================================
# CONFIG
# ==================================

st.set_page_config(
    page_title="HireSense AI",
    layout="wide",
    initial_sidebar_state="expanded"
)



# ==================================
# IMPORTS
# ==================================

from database.db import init_db

from modules.landing import landing_page
from modules.auth import auth_page
from modules.chat import main_page



# ==================================
# DATABASE
# ==================================

init_db()



# ==================================
# SESSION DEFAULTS
# ==================================

if "page" not in st.session_state:

    st.session_state.page = "landing"



if "login" not in st.session_state:

    st.session_state.login = False



if "username" not in st.session_state:

    st.session_state.username = "User"





# ==================================
# ROUTER
# ==================================


# LANDING

if st.session_state.page == "landing":


    landing_page()






# AUTH

elif st.session_state.page == "auth":


    if st.session_state.login == True:


        st.session_state.page = "main"

        st.rerun()


    else:


        auth_page()








# MAIN APP

elif st.session_state.page == "main":



    main_page()