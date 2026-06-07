import streamlit as st

import jwt


from streamlit_oauth import OAuth2Component


from database.db import (
    create_user,
    login_user
)





# ==================================================
# GOOGLE AUTH
# ==================================================


def google_login():


    oauth2 = OAuth2Component(

        client_id =
        st.secrets["google"]["client_id"],


        client_secret =
        st.secrets["google"]["client_secret"],



        authorize_endpoint =
        "https://accounts.google.com/o/oauth2/auth",



        token_endpoint =
        "https://oauth2.googleapis.com/token",



        refresh_token_endpoint =
        "https://oauth2.googleapis.com/token",



        revoke_token_endpoint =
        "https://oauth2.googleapis.com/revoke"

    )






    result = oauth2.authorize_button(

        name = "Continue with Google",


        redirect_uri =
        st.secrets["google"]["redirect_uri"],



        scope =
        "openid email profile",



        key =
        "google_login"

    )








    if result:



        token = result["token"]



        id_token = token["id_token"]





        user = jwt.decode(

            id_token,


            options={

                "verify_signature":False

            }

        )







        st.session_state.login=True



        st.session_state.username = user.get(

            "name",

            "Google User"

        )





        st.session_state.email = user.get(

            "email",

            ""

        )





        st.session_state.picture = user.get(

            "picture",

            ""

        )





        st.session_state.page="main"



        st.rerun()









# ==================================================
# AUTH PAGE
# ==================================================


def auth_page():



    # ---------------- CSS ----------------


    st.markdown(
        """
        <style>


        .block-container{

            max-width:430px;

            padding-top:85px;

        }




        .logo{

            width:52px;

            height:52px;

            background:#2563eb;

            color:white;

            border-radius:15px;


            display:flex;

            justify-content:center;

            align-items:center;


            margin:auto;


            font-weight:700;

            font-size:18px;

        }






        .title{

            text-align:center;

            margin-top:15px;

            font-size:28px;

            font-weight:700;

        }





        .subtitle{

            text-align:center;

            color:#9ca3af;

            font-size:14px;

            margin-bottom:30px;

        }





        div.stButton button{

            height:42px;

            border-radius:10px;

            font-size:14px;

        }



        </style>
        """,

        unsafe_allow_html=True

    )








    # ---------------- STATE ----------------



    if "auth_mode" not in st.session_state:


        st.session_state.auth_mode="login"









    # ---------------- HEADER ----------------



    st.markdown(

        """

       



        <div class="title">

        HireSense AI

        </div>




        <div class="subtitle">

        AI Interview Preparation Platform

        </div>

        """,

        unsafe_allow_html=True

    )










    # ==================================================
    # LOGIN
    # ==================================================


    if st.session_state.auth_mode=="login":




        email = st.text_input(

            "Email",

            key="login_email"

        )





        password = st.text_input(

            "Password",

            type="password",

            key="login_password"

        )








        if st.button(

            "Sign in",

            use_container_width=True

        ):





            user = login_user(

                email,

                password

            )






            if user:



                st.session_state.login=True



                st.session_state.username=user[1]



                st.session_state.email=user[2]



                st.session_state.page="main"



                st.rerun()





            else:



                st.error(

                    "Invalid email or password"

                )









        st.divider()








        # GOOGLE LOGIN


        google_login()










        if st.button(

            "Create new account",

            use_container_width=True

        ):



            st.session_state.auth_mode="register"



            st.rerun()










    # ==================================================
    # REGISTER
    # ==================================================


    else:




        name = st.text_input(

            "Full name"

        )






        email = st.text_input(

            "Email",

            key="register_email"

        )






        password = st.text_input(

            "Password",

            type="password",

            key="register_password"

        )








        if st.button(

            "Create account",

            use_container_width=True

        ):






            result = create_user(

                name,

                email,

                password

            )






            if result:




                st.success(

                    "Account created successfully"

                )





                st.session_state.auth_mode="login"




                st.rerun()







            else:



                st.error(

                    "Account already exists"

                )









        if st.button(

            "Already have account? Sign in",

            use_container_width=True

        ):




            st.session_state.auth_mode="login"



            st.rerun()