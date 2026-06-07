import streamlit as st


from database.db import (
    save_session,
    get_sessions,
    load_session
)



def sidebar():


    # ================= CSS =================

    st.markdown(
        """
        <style>


        [data-testid="stSidebar"]{

            background:#0b0f19;

        }


        section[data-testid="stSidebar"] > div:first-child{

            padding-top:8px !important;

        }


        [data-testid="stSidebar"] .element-container{

            margin-bottom:0px !important;

        }



        [data-testid="stSidebar"] button{


            height:21px !important;

            min-height:21px !important;

            background:transparent !important;

            border:none !important;

            border-radius:6px !important;

            padding:0px 8px !important;

            margin:0px !important;

        }


        /* remove space between menu items */

        [data-testid="stSidebar"] .element-container{

            margin-bottom:-4px !important;

        }



        [data-testid="stSidebar"] button div{

            justify-content:flex-start !important;

            width:100% !important;

        }


        [data-testid="stSidebar"] button p{

            text-align:left !important;
            
            font-size:12.5px !important;

            font-size:14px !important;

        }


        [data-testid="stSidebar"] button:hover{

            background:#1f2937 !important;

        }



        .brand{

            font-size:22px;

            font-weight:800;

            color:white;

        }


        .brand-sub{

            font-size:12px;

            color:#9ca3af;

            margin-bottom:18px;

        }



        .section-title{

            font-size:11px;

            color:#6b7280;

            font-weight:700;

            margin-top:12px;

            margin-bottom:5px;

            letter-spacing:.8px;

        }


        </style>
        """,

        unsafe_allow_html=True
    )



    with st.sidebar:



        # ================= BRAND =================


        st.markdown(
            """
            <div class="brand">
            HireSense AI
            </div>

            <div class="brand-sub">
            AI Interview Coach
            </div>
            """,

            unsafe_allow_html=True
        )



 
      # ================= PROFILE =================


        



        if "profile_open" not in st.session_state:


            st.session_state.profile_open=False




        username=st.session_state.get(

            "username",

            "User"

        )



        email=st.session_state.get(

            "email",

            "HireSense User"

        )





        col1,col2,col3=st.columns(

            [1,4,1]

        )



        with col1:


            st.write("👤")



        with col2:


            st.write(

                f"**{username}**"

            )



        with col3:



            if st.button(

                "⋯",

                key="profile_dropdown_btn"

            ):


                st.session_state.profile_open = (

                    not st.session_state.profile_open

                )





        if st.session_state.profile_open:


            st.caption(email)



            if st.button(

                "Sign out",

                use_container_width=True

            ):



                st.session_state.clear()



                st.session_state.page="landing"



                st.session_state.login=False



                st.rerun()





        # ================= WORKSPACE =================


        st.markdown(
            """
            <div class="section-title">
            WORKSPACE
            </div>
            """,
            unsafe_allow_html=True
        )



        if "current_menu" not in st.session_state:


            st.session_state.current_menu="Home"




        menu={


            "⌂  Home":"Home",

            "◇  Technical Interview":"Technical Interview",

            "☰  HR Interview":"HR Interview",

            "◫  Resume Analyzer":"Resume Analyzer",

            "</> Coding":"Coding Assessment",

            "◎  Mock Interview":"Mock Interview"


        }




        for label,page in menu.items():


            if st.button(

                label,

                use_container_width=True

            ):


                st.session_state.current_menu=page


                st.rerun()






 

      






  


       # ================= NEW SESSION =================
        st.markdown(
            """
            <div class="section-title">
            REFRESH
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "+ New Session",
            use_container_width=True
        ):


            current_page=st.session_state.get(
                "current_menu",
                "Home"
            )



            save_data={}



            for k,v in st.session_state.items():


                if k.startswith("history_"):

                    continue


                if k in [
                    "profile_open",
                    "profile_dropdown_btn"
                ]:

                    continue


                save_data[k]=v



            title=current_page




            if current_page=="Coding Assessment":


                title=f"Coding {st.session_state.get('coding_language','')} Q{st.session_state.get('question_no','')}"



            elif current_page=="Technical Interview":


                title=f"Technical - {st.session_state.get('tech_role','')} Q{st.session_state.get('tech_count','')}"



            elif current_page=="Mock Interview":


                title=f"Mock - {st.session_state.get('mock_role','')} Q{st.session_state.get('mock_count','')}"



            elif current_page=="HR Interview":


                title=f"HR - {st.session_state.get('hr_type','')} Q{st.session_state.get('hr_count','')}"



            elif current_page=="Resume Analyzer":


                title=f"Resume - {st.session_state.get('resume_role','')}"





            save_session(

                title,

                save_data,

                st.session_state.get(
                    "email",
                    None
                )

            )



            keep={}



            for k in [

                "username",

                "email",

                "login",

                "page"

            ]:


                if k in st.session_state:


                    keep[k]=st.session_state[k]



            st.session_state.clear()



            for k,v in keep.items():


                st.session_state[k]=v



            st.session_state.current_menu="Home"


            st.rerun()

         # ================= RECENTS =================


        st.markdown(
            """
            <div class="section-title">
            RECENTS
            </div>
            """,
            unsafe_allow_html=True
        )



        # fixed height scroll container

        history_container = st.container(
            height=180
        )



        with history_container:



            sessions=get_sessions(

                st.session_state.get(
                    "email",
                    None
                )

            )



            for item in sessions:



                if st.button(

                    item[1],

                    key=f"history_{item[0]}",

                    use_container_width=True

                ):



                    user_data={

                        "username":

                        st.session_state.get(
                            "username"
                        ),


                        "email":

                        st.session_state.get(
                            "email"
                        ),


                        "login":True

                    }




                    data=load_session(

                        item[0]

                    )



                    st.session_state.clear()



                    for k,v in data.items():


                        if not k.startswith(
                            "history_"
                        ):


                            st.session_state[k]=v



                    for k,v in user_data.items():


                        st.session_state[k]=v



                    st.rerun()







    return st.session_state.current_menu