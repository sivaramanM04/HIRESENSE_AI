import streamlit as st



def landing_page():


    st.markdown(
        """

<style>


/* APP BACKGROUND */

.stApp{

    background:#0b0f19;

    color:white;

}



/* REMOVE TOP SPACE */

.block-container{

    padding-top:30px;

}



/* HERO */


.hero{

    text-align:center;

    padding:40px 20px 25px 20px;

}



.title{

    font-size:58px;

    font-weight:800;

    letter-spacing:-1px;

}



.subtitle{

    margin-top:15px;

    font-size:17px;

    color:#9ca3af;

    line-height:1.6;

}





/* GET STARTED BUTTON */


div.stButton > button{


    height:45px !important;


    background:#2563eb !important;


    border:none !important;


    border-radius:12px !important;


    color:white !important;


    font-size:15px !important;


    font-weight:600 !important;


    margin-bottom:25px;


}



div.stButton > button:hover{

    background:#1d4ed8 !important;

}








/* FEATURE CARD */


.card{


    height:55px;


    background:#111827;


    border:1px solid #1f2937;


    border-radius:12px;


    padding:10px;


    display:flex;


    flex-direction:column;


    align-items:center;


    justify-content:center;


    transition:.2s;


}




.card:hover{

    border-color:#2563eb;

    transform:translateY(-2px);

}





.card h3{


    font-size:14px;


    font-weight:600;


    margin:0;


    color:white;


}




.card p{


    margin-top:4px;


    margin-bottom:0;


    font-size:11px;


    color:#9ca3af;


}






div[data-testid="column"]{

    padding:4px;

}



</style>


""",

        unsafe_allow_html=True
    )










    # ================= HERO =================


    st.markdown(
        """

<div class="hero">


<div class="title">

HireSense AI

</div>



<div class="subtitle">

Intelligent Interview Preparation Platform

<br>

Practice interviews, improve skills,
and prepare with AI guidance.


</div>


</div>

""",

        unsafe_allow_html=True

    )











    # ================= START =================


    if st.button(

        "Get Started",

        use_container_width=True

    ):


        st.session_state.started=True


        st.rerun()











    # ================= FEATURES ROW 1 =================


    c1,c2,c3 = st.columns(3)






    with c1:


        st.markdown(
            """

            <div class="card">

            <h3>
            Technical Interview
            </h3>

            <p>
            Role based practice
            </p>

            </div>

            """,
            unsafe_allow_html=True
        )








    with c2:


        st.markdown(
            """

            <div class="card">

            <h3>
            HR Interview
            </h3>

            <p>
            Communication skills
            </p>

            </div>

            """,
            unsafe_allow_html=True
        )









    with c3:


        st.markdown(
            """

            <div class="card">

            <h3>
            Resume Analyzer
            </h3>

            <p>
            ATS optimization
            </p>

            </div>

            """,
            unsafe_allow_html=True
        )












    # SMALL GAP


    st.write("")









    # ================= FEATURES ROW 2 =================


    empty1,c4,c5,empty2 = st.columns(

        [0.6,1,1,0.6]

    )








    with c4:


        st.markdown(
            """

            <div class="card">

            <h3>
            Coding Assessment
            </h3>

            <p>
            Code evaluation
            </p>

            </div>

            """,
            unsafe_allow_html=True
        )









    with c5:


        st.markdown(
            """

            <div class="card">

            <h3>
            Mock Interview
            </h3>

            <p>
            Real simulation
            </p>

            </div>

            """,
            unsafe_allow_html=True
        )