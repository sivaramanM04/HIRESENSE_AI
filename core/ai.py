import os

from dotenv import load_dotenv

from groq import Groq



load_dotenv()



client = Groq(

    api_key=os.getenv(
        "GROQ_API_KEY"
    )

)



def ask_ai(question):


    response = client.chat.completions.create(


        model="llama-3.3-70b-versatile",


        messages=[


            {

            "role":"system",

            "content":
            """
            You are HireSense AI.

            Act as an expert interview trainer.

            Help students with:
            Technical Interviews,
            HR Interviews,
            Resume Improvement,
            Coding rounds.
            """

            },


            {

            "role":"user",

            "content":question

            }

        ]

    )


    return response.choices[0].message.content