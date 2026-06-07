import streamlit as st


from core.ai import ask_ai

from components.ai_response import show_ai_response

from components.answer_box import answer_box


from database.db import save_history


from utils.score import extract_score

from utils.report import create_report







def technical_page():


    # ================= RESTORE HISTORY =================

    if "loaded_session" in st.session_state:


        data = st.session_state.loaded_session


        if data.get("current_menu") == "Technical Interview":


            for k,v in data.items():

                st.session_state[k] = v


        del st.session_state.loaded_session







    st.title(
        "Technical Interview"
    )


    st.caption(
        "AI powered technical preparation"
    )






    # ================= STATES =================


    if "tech_started" not in st.session_state:

        st.session_state.tech_started = False



    if "tech_question" not in st.session_state:

        st.session_state.tech_question = ""



    if "tech_count" not in st.session_state:

        st.session_state.tech_count = 0



    if "tech_answers" not in st.session_state:

        st.session_state.tech_answers = []



    if "tech_report" not in st.session_state:

        st.session_state.tech_report = None



    if "tech_result" not in st.session_state:

        st.session_state.tech_result = False



    if "tech_role" not in st.session_state:

        st.session_state.tech_role = ""



    if "tech_level" not in st.session_state:

        st.session_state.tech_level = ""




    # IMPORTANT FOR SIDEBAR HISTORY

    st.session_state.current_menu = "Technical Interview"








    # ================= RESULT PAGE =================


    if st.session_state.tech_result:



        st.title(
            "Technical Interview Result"
        )



        show_ai_response(
            "Final Report",
            st.session_state.tech_report
        )




        pdf = create_report(

            "Technical Report",

            st.session_state.tech_report

        )





        with open(pdf,"rb") as file:



            st.download_button(

                "Download PDF",

                file,

                "technical_report.pdf",

                use_container_width=True

            )






        if st.button(

            "Finish Interview",

            use_container_width=True

        ):



            st.session_state.tech_started=False

            st.session_state.tech_result=False

            st.session_state.tech_count=0

            st.session_state.tech_question=""

            st.session_state.tech_answers=[]

            st.session_state.tech_report=None

            st.session_state.tech_role=""

            st.session_state.tech_level=""




            st.rerun()



        return










    # ================= START PAGE =================


    if not st.session_state.tech_started:




        role = st.text_input(

            "Target Role",

            placeholder="Python Developer"

        )




        level = st.selectbox(

            "Difficulty",

            [

                "Beginner",

                "Intermediate",

                "Advanced"

            ]

        )








        if st.button(

            "Start Interview",

            use_container_width=True

        ):



            if role.strip()=="":



                st.warning(
                    "Enter role"
                )


                st.stop()








            question = ask_ai(

                f"""

                Act as technical interviewer.


                Role:
                {role}


                Level:
                {level}



                Ask first technical question only.


                No answer.

                No HTML.

                """

            )







            st.session_state.tech_role = role

            st.session_state.tech_level = level

            st.session_state.tech_question = question

            st.session_state.tech_count = 1

            st.session_state.tech_answers = []

            st.session_state.tech_started = True

            st.session_state.current_menu = (
                "Technical Interview"
            )



            st.rerun()












    # ================= QUESTION PAGE =================


    if st.session_state.tech_started:



        st.subheader(

            st.session_state.tech_role

        )




        st.progress(

            st.session_state.tech_count / 10

        )





        st.caption(

            f"Question {st.session_state.tech_count}/10"

        )







        with st.container(border=True):


            st.markdown(

                st.session_state.tech_question

            )







        answer = answer_box(

            f"technical_answer_{st.session_state.tech_count}"

        )







        if st.button(

            "Submit Answer",

            use_container_width=True

        ):




            if len(answer.strip()) < 5:



                st.error(

                    "Please write answer"

                )


                st.stop()









            st.session_state.tech_answers.append(

                {

                    "question":

                    st.session_state.tech_question,


                    "answer":

                    answer

                }

            )










            # NEXT QUESTION


            if st.session_state.tech_count < 10:




                question = ask_ai(

                    f"""

                    Continue technical interview.



                    Previous answers:


                    {st.session_state.tech_answers}



                    Ask next different question only.


                    No HTML.

                    """

                )






                st.session_state.tech_question = question


                st.session_state.tech_count += 1





                st.rerun()












            # FINAL RESULT


            else:




                report = ask_ai(

                    f"""

                    Evaluate complete technical interview.



                    {st.session_state.tech_answers}




                    Give:


                    ## Overall Score

                    x/10



                    ## Strengths



                    ## Mistakes



                    ## Improvement Plan



                    ## Hiring Decision



                    No HTML.

                    """

                )






                st.session_state.tech_report = report


                st.session_state.tech_result = True







                score = extract_score(

                    report

                )






                save_history(

                    "Technical Interview",

                    st.session_state.tech_role,

                    score

                )






                st.rerun()