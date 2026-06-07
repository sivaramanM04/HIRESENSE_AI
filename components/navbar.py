import streamlit as st


# =================================
# NAVBAR
# =================================

def navbar():


    # ---------- CSS ----------

    st.markdown(
        """
        <style>

        .block-container {
            padding-top: 15px !important;
        }


        .navbar-title {
            text-align:center;
            font-size:22px;
            font-weight:700;
            color:white;
            margin-top:-10px;
        }


        .navbar-sub {
            text-align:center;
            font-size:12px;
            color:#9ca3af;
        }



        div[data-testid="stPopover"] button {

            width:42px;
            height:42px;

            border-radius:50%;

            background:#2563eb;

            color:white;

            border:none;

            font-weight:700;
        }


        .profile-name {

            font-size:15px;
            font-weight:700;

        }


        .profile-mail {

            font-size:12px;
            color:#9ca3af;

        }


        </style>
        """,
        unsafe_allow_html=True
    )




    # ---------- USER DATA ----------


    username = st.session_state.get(
        "username",
        "User"
    )


    email = st.session_state.get(
        "email",
        "user@gmail.com"
    )


    picture = st.session_state.get(
        "picture",
        None
    )




    # ---------- NAV LAYOUT ----------


    left, center, right = st.columns(
        [2,6,1]
    )




    with center:


        st.markdown(
            """
            <div class="navbar-title">
                HireSense AI
            </div>

            <div class="navbar-sub">
                AI Interview Preparation Platform
            </div>
            """,
            unsafe_allow_html=True
        )






    # ---------- PROFILE ----------


    with right:


        with st.popover(
            username[0].upper()
        ):



            if picture:


                st.image(
                    picture,
                    width=55
                )


            else:


                st.write(
                    "👤"
                )



            st.markdown(
                f"""
                <p class="profile-name">
                {username}
                </p>

                <p class="profile-mail">
                {email}
                </p>
                """,
                unsafe_allow_html=True
            )



            st.divider()



            if st.button(
                "Account",
                use_container_width=True
            ):


                st.info(
                    "Coming soon"
                )




            if st.button(
                "Sign out",
                use_container_width=True
            ):


                st.session_state.clear()


                st.session_state.page = "landing"


                st.session_state.login = False


                st.rerun()




    st.divider()