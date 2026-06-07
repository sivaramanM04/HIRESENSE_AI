import streamlit as st

from core.ai import ask_ai

from utils.pdf_reader import read_pdf

from components.ai_response import show_ai_response

from database.db import save_history

from utils.score import extract_score



def resume_page():


    st.title(
        "Resume Analyzer"
    )


    st.caption(
        "AI powered ATS + Resume Interview Preparation"
    )



    # ---------------- SESSION STATES ----------------


    if "resume_text" not in st.session_state:

        st.session_state.resume_text = ""


    if "resume_role" not in st.session_state:

        st.session_state.resume_role = ""


    if "resume_report" not in st.session_state:

        st.session_state.resume_report = None


    if "resume_questions" not in st.session_state:

        st.session_state.resume_questions = None


    if "show_resume_result" not in st.session_state:

        st.session_state.show_resume_result = False


    if "show_resume_questions" not in st.session_state:

        st.session_state.show_resume_questions = False





    # ---------------- QUESTIONS PAGE ----------------


    if st.session_state.show_resume_questions:


        st.title(
            "Resume Interview Preparation"
        )


        show_ai_response(

            "Interview Questions With Answers",

            st.session_state.resume_questions

        )



        if st.button(

            "Back To Resume Report",

            use_container_width=True

        ):


            st.session_state.show_resume_questions = False


            st.rerun()



        return






    # ---------------- RESULT PAGE ----------------


    if st.session_state.show_resume_result:



        st.title(
            "Resume Analysis Result"
        )



        show_ai_response(

            "ATS Resume Report",

            st.session_state.resume_report

        )



        st.divider()



        if st.button(

            "Generate Interview Questions",

            use_container_width=True

        ):




            questions = ask_ai(

                f"""

                Act as a senior technical interviewer.



                Analyze this candidate resume:



                {st.session_state.resume_text}




                Target Role:


                {st.session_state.resume_role}






                Generate resume based interview preparation.



                Create exactly 10 questions with answers.



                Cover:



                - Candidate introduction

                - Resume skills

                - Projects

                - Technologies

                - Problem solving

                - HR questions







                Format:



                ## Question 1


                Write interview question




                ### Answer


                Write professional answer





                ## Question 2


                Write interview question




                ### Answer


                Write professional answer






                Continue until Question 10.







                Rules:


                - Answers should be interview ready


                - Use candidate resume details


                - No HTML


                - Clean markdown only

                """

            )




            st.session_state.resume_questions = questions


            st.session_state.show_resume_questions = True



            st.rerun()






        if st.button(

            "Finish",

            use_container_width=True

        ):



            st.session_state.resume_text = ""


            st.session_state.resume_role = ""


            st.session_state.resume_report = None


            st.session_state.resume_questions = None


            st.session_state.show_resume_result = False


            st.session_state.show_resume_questions = False



            st.rerun()





        return







    # ---------------- UPLOAD PAGE ----------------


    role = st.text_input(

        "Target Job Role",

        placeholder="Example: Python Developer"

    )



    resume = st.file_uploader(

        "Upload Resume PDF",

        type=["pdf"]

    )






    if st.button(

        "Analyze Resume",

        use_container_width=True

    ):




        if resume is None:


            st.error(

                "Please upload your resume"

            )


            st.stop()





        if role.strip() == "":


            st.error(

                "Please enter target role"

            )


            st.stop()







        resume_text = read_pdf(

            resume

        )



        st.session_state.resume_text = resume_text


        st.session_state.resume_role = role








        report = ask_ai(

            f"""

            Act as a professional ATS resume analyzer.




            Resume:


            {resume_text}





            Applying Role:


            {role}






            Analyze resume and provide:






            ## ATS Score

            x/10






            ## Candidate Summary







            ## Matching Skills


            - points







            ## Missing Skills


            - points








            ## Project Analysis


            - points








            ## Resume Weakness


            - points








            ## Improvement Suggestions


            - points









            ## Interview Preparation Plan


            - points








            Rules:


            No HTML.


            Clean markdown only.

            """

        )








        st.session_state.resume_report = report



        st.session_state.show_resume_result = True








        score = extract_score(

            report

        )







        save_history(

            "Resume Analyzer",

            role,

            score

        )








        st.rerun()