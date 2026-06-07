import streamlit as st


from database.db import get_history



def history_page():


    st.title(

        "📚 Interview History"

    )


    data=get_history(

        st.session_state.email

    )


    for item in data:


        st.info(

            f"""

Type:

{item[2]}


Score:

{item[3]}


Feedback:

{item[4]}

"""

        )