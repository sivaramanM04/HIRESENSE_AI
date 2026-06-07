import plotly.graph_objects as go


def skill_chart():


    skills = [

        "Python",

        "SQL",

        "Communication",

        "Problem Solving",

        "Projects"

    ]


    scores=[

        85,

        70,

        80,

        75,

        90

    ]



    fig = go.Figure()


    fig.add_trace(

        go.Scatterpolar(

            r=scores,

            theta=skills,

            fill="toself"

        )

    )


    fig.update_layout(

        polar=dict(

            radialaxis=dict(

                visible=True,

                range=[0,100]

            )

        )

    )


    return fig