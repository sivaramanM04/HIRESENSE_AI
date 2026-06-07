import streamlit as st

from core.ai import ask_ai

from components.ai_response import show_ai_response

from components.answer_box import answer_box

from database.db import save_history

from utils.score import extract_score




def mock_page():


    # ================= RESTORE HISTORY =================

    if "loaded_session" in st.session_state:


        data = st.session_state.loaded_session


        if data.get("current_menu") == "Mock Interview":


            for k,v in data.items():

                st.session_state[k] = v


        del st.session_state.loaded_session







    st.title(
        "Mock Interview"
    )


    st.caption(
        "AI powered real interview simulation"
    )







    # ================= STATES =================


    if "mock_started" not in st.session_state:

        st.session_state.mock_started=False



    if "mock_question" not in st.session_state:

        st.session_state.mock_question=""



    if "mock_count" not in st.session_state:

        st.session_state.mock_count=0



    if "mock_answers" not in st.session_state:

        st.session_state.mock_answers=[]



    if "mock_report" not in st.session_state:

        st.session_state.mock_report=None



    if "mock_result" not in st.session_state:

        st.session_state.mock_result=False



    if "mock_role" not in st.session_state:

        st.session_state.mock_role=""



    if "mock_level" not in st.session_state:

        st.session_state.mock_level=""





    # IMPORTANT FOR HISTORY

    st.session_state.current_menu="Mock Interview"









    # ================= RESULT PAGE =================


    if st.session_state.mock_result:



        st.title(
            "Mock Interview Result"
        )



        show_ai_response(

            "Final Interview Report",

            st.session_state.mock_report

        )






        if st.button(

            "Finish Interview",

            use_container_width=True

        ):



            st.session_state.mock_started=False

            st.session_state.mock_question=""

            st.session_state.mock_count=0

            st.session_state.mock_answers=[]

            st.session_state.mock_report=None

            st.session_state.mock_result=False

            st.session_state.mock_role=""

            st.session_state.mock_level=""



            st.rerun()




        return










    # ================= START PAGE =================


    if not st.session_state.mock_started:




        role = st.text_input(

            "Interview Role",

            placeholder="Example: Data Analyst"

        )




        difficulty = st.selectbox(

            "Difficulty",

            [

                "Beginner",

                "Intermediate",

                "Advanced"

            ]

        )







        if st.button(

            "Start Mock Interview",

            use_container_width=True

        ):




            if role.strip()=="":


                st.warning(

                    "Please enter role"

                )


                st.stop()








            question = ask_ai(

                f"""

                Act as a real company interviewer.


                Role:

                {role}


                Difficulty:

                {difficulty}


                Start interview.


                Ask first question only.


                Mix:

                Technical

                HR

                Scenario


                No answer.

                No HTML.

                """

            )








            st.session_state.mock_role=role

            st.session_state.mock_level=difficulty

            st.session_state.mock_question=question

            st.session_state.mock_count=1

            st.session_state.mock_started=True

            st.session_state.mock_answers=[]


            st.session_state.current_menu="Mock Interview"




            st.rerun()












    # ================= INTERVIEW PAGE =================


    if st.session_state.mock_started:




        st.subheader(

            f"{st.session_state.mock_role} Interview"

        )




        st.progress(

            st.session_state.mock_count/5

        )




        st.caption(

            f"Question {st.session_state.mock_count}/5"

        )







        with st.container(border=True):


            st.markdown(
                "### Interviewer"
            )


            st.markdown(

                st.session_state.mock_question

            )








        answer = answer_box(

            f"mock_answer_{st.session_state.mock_count}"

        )








        if st.button(

            "Submit Answer",

            use_container_width=True

        ):




            if len(answer.strip()) < 5:



                st.error(

                    "Please write your answer"

                )


                st.stop()









            st.session_state.mock_answers.append(

                {

                    "question":

                    st.session_state.mock_question,


                    "answer":

                    answer

                }

            )









            # NEXT QUESTION


            if st.session_state.mock_count < 5:





                question = ask_ai(

                    f"""

                    Continue mock interview.


                    Role:

                    {st.session_state.mock_role}



                    Previous:

                    {st.session_state.mock_answers}



                    Ask next interview question only.


                    Mix technical, HR and situation.


                    No HTML.

                    """

                )








                st.session_state.mock_question=question


                st.session_state.mock_count+=1




                st.rerun()












            # FINAL REPORT


            else:





                report = ask_ai(

                    f"""

                    Analyze full mock interview.



                    Answers:

                    {st.session_state.mock_answers}



                    Provide:


                    ## Overall Score

                    x/10


                    ## Technical Knowledge

                    x/10


                    ## Communication Skill

                    x/10


                    ## Problem Solving

                    x/10


                    ## Strengths


                    ## Weakness


                    ## Improvement Roadmap


                    ## Hiring Decision


                    No HTML.

                    """

                )








                st.session_state.mock_report=report

                st.session_state.mock_result=True








                score = extract_score(

                    report

                )








                save_history(

                    "Mock Interview",

                    st.session_state.mock_role,

                    score

                )








                st.rerun()