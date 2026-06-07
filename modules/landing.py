import streamlit as st


def landing_page():


    st.markdown(
        """

        <style>

        .title{
        text-align:center;
        font-size:60px;
        font-weight:bold;
        margin-top:100px;
        }

        .subtitle{
        text-align:center;
        font-size:22px;
        color:gray;
        }

        </style>


        <div class='title'>
        HireSense AI
        </div>


        <div class='subtitle'>

        Intelligent Interview Preparation Platform

        <br><br>

        Prepare Technical, HR, Resume and Coding Interviews

        </div>

        """,
        unsafe_allow_html=True
    )


    st.write("")


    c1,c2,c3 = st.columns([2,1,2])


    with c2:


        if st.button(
            "Get Started",
            use_container_width=True
        ):

            st.session_state.page="auth"

            st.rerun()