import streamlit as st


from components.sidebar import sidebar


from core.ai import ask_ai


from modules.technical import technical_page
from modules.hr import hr_page
from modules.resume import resume_page
from modules.coding import coding_page
from modules.mock import mock_page
from modules.dashboard import dashboard_page




# ==================================================
# HOME PAGE
# ==================================================

def home_page():
    


    # ================= STYLE =================


    st.markdown(
        """
        <style>

        


        html, body, [class*="css"]{

            font-family:Inter, sans-serif;

        }


        .block-container{

            padding-top:15px;

            max-width:1100px;

        }



        .home-title{

            text-align:center;

            font-size:34px;

            font-weight:800;

            margin-top:20px;

        }



        .home-sub{

            text-align:center;

            color:#9ca3af;

            font-size:15px;

            margin-bottom:35px;

        }





        div.stButton > button{

            height:34px;

            background:#18181b;

            border:1px solid #303030;

            border-radius:16px;

            font-size:11px;

            transition:.2s;

        }





        div.stButton > button:hover{


            border-color:#10b981;


            background:#202020;


        }




        </style>
        """,

        unsafe_allow_html=True
    )








    # ================= HERO =================


    st.markdown(
        """

        <div class="home-title">

        AI Interview Workspace

        </div>


        <div class="home-sub">

        Practice, analyze and improve your interview performance

        </div>

        """,

        unsafe_allow_html=True
    )










    # ================= QUICK ACTIONS =================


    st.markdown(
        "### Select practice area"
    )



    col1,col2,col3 = st.columns(3)





    with col1:


        if st.button(

            "Technical\nInterview",

            use_container_width=True

        ):


            st.session_state.current_menu="Technical Interview"

            st.rerun()









    with col2:


        if st.button(

            "HR\nRound",

            use_container_width=True

        ):


            st.session_state.current_menu="HR Interview"


            st.rerun()







    with col3:


        if st.button(

            "Resume\nAnalyzer",

            use_container_width=True

        ):


            st.session_state.current_menu="Resume Analyzer"


            st.rerun()









    _,col4,col5,_= st.columns([0.5,1,1,0.5])






    with col4:


        if st.button(

            "Coding\nProblem",

            use_container_width=True

        ):


            st.session_state.current_menu="Coding Assessment"

            st.rerun()








    with col5:


        if st.button(

            "Mock\nInterview",

            use_container_width=True

        ):


            st.session_state.current_menu="Mock Interview"

            st.rerun()









    


    st.write("")







    # ================= CHAT =================


    if "messages" not in st.session_state:


        st.session_state.messages=[]







    for msg in st.session_state.messages:


        with st.chat_message(

            msg["role"]

        ):


            st.markdown(

                msg["content"]

            )








    user = st.chat_input(

        "Ask your interview question..."

    )







    if user:



        st.session_state.messages.append(

            {

                "role":"user",

                "content":user

            }

        )





        answer = ask_ai(

            user

        )






        st.session_state.messages.append(

            {

                "role":"assistant",

                "content":answer

            }

        )




        st.rerun()













# ==================================================
# MAIN ROUTER
# ==================================================

def main_page():



    # ================= NAVBAR =================








    # ================= SIDEBAR =================

    page = sidebar()









    # ================= ROUTING =================


    if page=="Home":


        home_page()








    elif page=="Dashboard":


        dashboard_page()








    elif page=="Technical Interview":


        technical_page()








    elif page=="HR Interview":


        hr_page()









    elif page=="Resume Analyzer":


        resume_page()








    elif page=="Coding Assessment":


        coding_page()








    elif page=="Mock Interview":


        mock_page()