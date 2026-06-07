import streamlit as st

from core.ai import ask_ai

from components.ai_response import show_ai_response

from components.answer_box import answer_box

from database.db import save_history

from utils.score import extract_score





def hr_page():


    # ================= RESTORE HISTORY =================

    if "loaded_session" in st.session_state:


        data = st.session_state.loaded_session


        if data.get("current_menu") == "HR Interview":


            for k,v in data.items():

                st.session_state[k] = v


        del st.session_state.loaded_session






    st.title(
        "HR Interview"
    )


    st.caption(
        "AI powered HR interview simulation"
    )







    # ================= STATES =================


    if "hr_started" not in st.session_state:

        st.session_state.hr_started = False



    if "hr_question" not in st.session_state:

        st.session_state.hr_question = ""



    if "hr_count" not in st.session_state:

        st.session_state.hr_count = 0



    if "hr_answers" not in st.session_state:

        st.session_state.hr_answers = []



    if "hr_report" not in st.session_state:

        st.session_state.hr_report = None



    if "hr_result" not in st.session_state:

        st.session_state.hr_result = False



    if "hr_type" not in st.session_state:

        st.session_state.hr_type = ""



    if "hr_level" not in st.session_state:

        st.session_state.hr_level = ""






    # IMPORTANT FOR SIDEBAR HISTORY

    st.session_state.current_menu = "HR Interview"









    # ================= RESULT PAGE =================


    if st.session_state.hr_result:



        st.title(
            "HR Interview Result"
        )



        show_ai_response(

            "Final HR Report",

            st.session_state.hr_report

        )







        if st.button(

            "Finish Interview",

            use_container_width=True

        ):



            st.session_state.hr_started=False

            st.session_state.hr_question=""

            st.session_state.hr_count=0

            st.session_state.hr_answers=[]

            st.session_state.hr_report=None

            st.session_state.hr_result=False

            st.session_state.hr_type=""

            st.session_state.hr_level=""



            st.rerun()




        return












    # ================= START PAGE =================


    if not st.session_state.hr_started:




        experience = st.selectbox(

            "Experience Level",

            [
                "Fresher",
                "Experienced"
            ]

        )





        interview_type = st.selectbox(

            "Interview Type",

            [

                "General HR",

                "Behavioral",

                "Stress Interview",

                "Managerial"

            ]

        )








        if st.button(

            "Start HR Interview",

            use_container_width=True

        ):






            question = ask_ai(

                f"""

                Act as professional HR interviewer.


                Candidate:

                {experience}


                Interview:

                {interview_type}



                Ask first HR interview question only.


                No answer.

                No HTML.

                """

            )








            st.session_state.hr_question = question


            st.session_state.hr_type = interview_type


            st.session_state.hr_level = experience


            st.session_state.hr_count = 1


            st.session_state.hr_started = True


            st.session_state.hr_answers = []


            st.session_state.current_menu="HR Interview"





            st.rerun()














    # ================= QUESTION PAGE =================


    if st.session_state.hr_started:





        st.subheader(

            st.session_state.hr_type

        )





        st.progress(

            st.session_state.hr_count / 5

        )




        st.caption(

            f"Question {st.session_state.hr_count}/5"

        )







        with st.container(border=True):


            st.markdown(

                st.session_state.hr_question

            )








        answer = answer_box(

            f"hr_answer_{st.session_state.hr_count}"

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










            st.session_state.hr_answers.append(

                {

                    "question":

                    st.session_state.hr_question,


                    "answer":

                    answer

                }

            )









            # NEXT QUESTION


            if st.session_state.hr_count < 5:




                question = ask_ai(

                    f"""

                    Continue HR interview.


                    Previous:

                    {st.session_state.hr_answers}


                    Ask next different HR question only.

                    No HTML.

                    """

                )






                st.session_state.hr_question = question


                st.session_state.hr_count += 1



                st.rerun()












            # FINAL REPORT


            else:




                report = ask_ai(

                    f"""

                    Evaluate HR interview:


                    {st.session_state.hr_answers}



                    Provide:


                    ## Overall Score

                    x/10


                    ## Communication Skill

                    x/10


                    ## Confidence

                    x/10


                    ## STAR Method Analysis


                    ## Strengths


                    ## Weakness


                    ## Improvement Tips


                    ## Hiring Recommendation


                    No HTML.

                    """

                )







                st.session_state.hr_report = report


                st.session_state.hr_result = True








                score = extract_score(

                    report

                )







                save_history(

                    "HR Interview",

                    st.session_state.hr_type,

                    score

                )






                st.rerun()