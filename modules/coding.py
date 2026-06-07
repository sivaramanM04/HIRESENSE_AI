import streamlit as st

from streamlit_ace import st_ace

from core.ai import ask_ai

from components.ai_response import show_ai_response

from database.db import save_history

from utils.score import extract_score



# ---------------- STARTER CODE ----------------


def starter_code(language):


    if language == "Python":

        return """
def solution():

    pass
"""


    elif language == "Java":

        return """
class Main {


    public static void main(String[] args){


    }

}
"""


    elif language == "JavaScript":

        return """
function solution(){


}
"""


    elif language == "SQL":

        return """
SELECT


FROM


WHERE

;
"""


    elif language == "C++":

        return """
#include <iostream>

using namespace std;


int main(){


    return 0;

}
"""


    return ""





# ---------------- EDITOR LANGUAGE ----------------


def ace_language(language):


    if language == "C++":

        return "c_cpp"


    return language.lower()






# ---------------- MAIN ----------------


def coding_page():


    st.title(
        "Coding Assessment"
    )


    st.caption(
        "AI powered coding interview"
    )

        # ---------- RESTORE FROM HISTORY ----------

    if "loaded_session" in st.session_state:


        data = st.session_state.loaded_session


        if data.get("page") == "Coding Assessment":


            st.session_state.coding_started = data.get(
                "coding_started",
                False
            )


            st.session_state.question_no = data.get(
                "question_no",
                0
            )


            st.session_state.coding_question = data.get(
                "coding_question",
                ""
            )


            st.session_state.coding_answers = data.get(
                "coding_answers",
                []
            )


            st.session_state.coding_report = data.get(
                "coding_report",
                None
            )


            st.session_state.show_coding_result = data.get(
                "show_coding_result",
                False
            )


            st.session_state.coding_language = data.get(
                "coding_language",
                ""
            )


            st.session_state.coding_level = data.get(
                "coding_level",
                ""
            )


            del st.session_state.loaded_session



    # ---------- SESSION ----------


    if "coding_started" not in st.session_state:

        st.session_state.coding_started = False


    if "question_no" not in st.session_state:

        st.session_state.question_no = 0


    if "coding_question" not in st.session_state:

        st.session_state.coding_question = ""


    if "coding_answers" not in st.session_state:

        st.session_state.coding_answers = []


    if "coding_report" not in st.session_state:

        st.session_state.coding_report = None


    if "show_coding_result" not in st.session_state:

        st.session_state.show_coding_result = False


    if "coding_language" not in st.session_state:

        st.session_state.coding_language = ""


    if "coding_level" not in st.session_state:

        st.session_state.coding_level = ""

    st.session_state.messages = [
        {
            "role":"system",

            "content":"Coding Assessment"
        }
    ]


    st.session_state.module_data = {

        "page":
        "Coding Assessment",


        "coding_started":
        st.session_state.coding_started,


        "question_no":
        st.session_state.question_no,


        "coding_question":
        st.session_state.coding_question,


        "coding_answers":
        st.session_state.coding_answers,


        "coding_report":
        st.session_state.coding_report,


        "show_coding_result":
        st.session_state.show_coding_result,


        "coding_language":
        st.session_state.coding_language,


        "coding_level":
        st.session_state.coding_level

    }





    # ---------- RESULT PAGE ----------


    if st.session_state.show_coding_result:


        st.title(
            "Coding Assessment Result"
        )


        show_ai_response(

            "Final Coding Report",

            st.session_state.coding_report

        )



        if st.button(

            "Finish Assessment",

            use_container_width=True

        ):


            st.session_state.coding_started = False

            st.session_state.show_coding_result = False

            st.session_state.question_no = 0

            st.session_state.coding_question = ""

            st.session_state.coding_answers = []

            st.session_state.coding_report = None


            st.rerun()



        return






    # ---------- START PAGE ----------


    if not st.session_state.coding_started:



        language = st.selectbox(

            "Programming Language",

            [

                "Python",

                "Java",

                "JavaScript",

                "C++",

                "SQL"

            ]

        )



        level = st.selectbox(

            "Difficulty",

            [

                "Easy",

                "Medium",

                "Hard"

            ]

        )



        if st.button(

            "Start Assessment",

            use_container_width=True

        ):



            question = ask_ai(

                f"""

                Act as coding interviewer.


                Language:

                {language}


                Difficulty:

                {level}



                Generate first coding question.


                Include:

                Problem Statement

                Input

                Output

                Example



                Do not provide solution.

                No HTML.

                """

            )



            st.session_state.coding_language = language

            st.session_state.coding_level = level

            st.session_state.coding_question = question

            st.session_state.question_no = 1

            st.session_state.coding_answers = []

            st.session_state.coding_report = None

            st.session_state.coding_started = True



            st.rerun()






    # ---------- TEST PAGE ----------


    if st.session_state.coding_started:



        st.subheader(

            f"{st.session_state.coding_language} Assessment"

        )


        st.progress(

            st.session_state.question_no / 2

        )


        st.caption(

            f"Question {st.session_state.question_no} of 2"

        )




        with st.container(border=True):


            st.markdown(

                st.session_state.coding_question

            )





        code = st_ace(


            value=starter_code(

                st.session_state.coding_language

            ),


            language=ace_language(

                st.session_state.coding_language

            ),


            theme="monokai",


            height=350,


            key=f"editor_{st.session_state.question_no}"


        )





        if st.button(

            "Submit Code",

            use_container_width=True

        ):



            if code is None or len(code.strip()) < 20:


                st.error(

                    "Please write valid code"

                )


                st.stop()





            st.session_state.coding_answers.append(

                {

                    "question":

                    st.session_state.coding_question,


                    "answer":

                    code

                }

            )






            # QUESTION 2


            if st.session_state.question_no < 2:



                question = ask_ai(

                    f"""

                    Generate another coding question.


                    Language:

                    {st.session_state.coding_language}


                    Difficulty:

                    {st.session_state.coding_level}


                    Make it different.


                    No solution.

                    """

                )



                st.session_state.coding_question = question

                st.session_state.question_no += 1



                st.rerun()








            # FINAL REPORT


            else:



                report = ask_ai(

                    f"""

                    Evaluate coding test.


                    Language:

                    {st.session_state.coding_language}



                    Answers:


                    {st.session_state.coding_answers}




                    Provide:


                    ## Score

                    x/10


                    ## Correctness


                    ## Code Quality


                    ## Time Complexity


                    ## Space Complexity


                    ## Mistakes


                    ## Improvement Tips



                    No HTML.

                    """

                )




                st.session_state.coding_report = report


                st.session_state.show_coding_result = True



                score = extract_score(

                    report

                )



                save_history(

                    "Coding Assessment",

                    st.session_state.coding_language,

                    score

                )



                st.rerun()