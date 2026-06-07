import os


from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)


from reportlab.lib.styles import (
    getSampleStyleSheet
)




def create_report(title,content):


    if not os.path.exists("reports"):

        os.makedirs("reports")



    path = "reports/interview_report.pdf"



    pdf = SimpleDocTemplate(

        path

    )



    styles = getSampleStyleSheet()


    elements=[]



    elements.append(

        Paragraph(

            title,

            styles["Title"]

        )

    )



    elements.append(

        Spacer(1,20)

    )



    for line in content.split("\n"):


        elements.append(

            Paragraph(

                line,

                styles["BodyText"]

            )

        )



    pdf.build(

        elements

    )



    return path