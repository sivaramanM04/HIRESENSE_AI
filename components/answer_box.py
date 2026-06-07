import streamlit as st



def answer_box(key):


    answer = st.text_area(

        label="Your Answer",

        placeholder="Write your detailed answer here...",

        height=220,

        key=key

    )


    return answer