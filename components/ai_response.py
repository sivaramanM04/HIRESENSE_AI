import streamlit as st



def show_ai_response(title, response):


    st.divider()


    st.markdown(
        f"## {title}"
    )


    # clean unwanted html

    clean_response = (

        response

        .replace("<div>", "")

        .replace("</div>", "")

        .replace("<b>", "**")

        .replace("</b>", "**")

        .replace("<br>", "\n")

    )


    with st.container(border=True):


        st.markdown(

            clean_response

        )