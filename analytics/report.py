from reportlab.pdfgen import canvas


def create_report():

    path="interview_report.pdf"


    pdf=canvas.Canvas(
        path
    )


    pdf.setTitle(
        "HireSense AI Report"
    )



    pdf.drawString(

        100,

        750,

        "HireSense AI Interview Report"

    )



    pdf.drawString(

        100,

        700,

        "Technical Score: 85/100"

    )



    pdf.drawString(

        100,

        670,

        "Communication Score: 80/100"

    )



    pdf.drawString(

        100,

        640,

        "Recommendation: Ready for Interview"

    )


    pdf.save()


    return path