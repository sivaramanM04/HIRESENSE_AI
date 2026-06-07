import streamlit as st

from database.db import get_history



def dashboard_page():


    st.title(
        "Performance Dashboard"
    )


    data = get_history()



    total = len(data)



    scores=[]


    for row in data:


        try:

            value = int(
                row[3].split("/")[0]
            )


            scores.append(value)


        except:

            pass




    average = (

        sum(scores) / len(scores)

        if scores

        else 0

    )



    c1,c2,c3 = st.columns(3)



    c1.metric(

        "Total Sessions",

        total

    )


    c2.metric(

        "Average Score",

        f"{average:.1f}/10"

    )


    c3.metric(

        "Reports",

        total

    )



    st.divider()



    st.subheader(

        "Performance"

    )



    for row in data[:5]:


        st.write(

            row[1]

        )


        try:

            value=int(

                row[3].split("/")[0]

            )


            st.progress(

                value/10

            )


        except:

            pass




    st.divider()



    st.subheader(

        "Recent Activity"

    )



    for row in data[:10]:


        st.write(

            f"{row[1]}  | Score: {row[3]}"

        )