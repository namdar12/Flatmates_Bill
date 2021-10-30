from fpdf import FPDF
import os


class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates
    such as their names, their due amount, and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, *args, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='c', ln=1)

        # Insert period label and values
        pdf.cell(w=100, h=40, txt="Period: ", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        #Insert the name and pay amount for each flatmate
        for flat in args:
            pdf.set_font(family='Times', size=14, style='I')
            pdf.cell(w=100,h=40,txt=flat.name, border =0)
            pdf.cell(w=150, h=40, txt=str(flat.pays(bill,*args)), border=0, ln=1)

        pdf.output(f"{self.filename}.pdf")
        #webbrowser.open('file://' + os.path.realpath(self.filename))