from fpdf import FPDF


class Bill:
    """
    Object that contains data about a bill, such as
    total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the flat
    and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * float(weight)
        return to_pay


class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates
    such as their names, their due amount, and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='c', ln=1)

        # Insert period label and values
        pdf.cell(w=100, h=40, txt="Period: ", border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        #Insert the name and pay amount for each flatmate
        pdf.cell(w=100,h=40,txt=flatmate1.name, border =1)
        pdf.cell(w=150, h=40, txt=str(flatmate1.pays(bill,flatmate2)), border=1, ln=1)

        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=40, txt=str(flatmate2.pays(bill, flatmate1)), border=1, ln=1)

        pdf.output(self.filename + '.pdf')


electric_bill = Bill(120, "March 2020")
John = Flatmate("John", 20)
Smith = Flatmate("Smith", 25)

print(John.pays(electric_bill, flatmate2=Smith))
print(Smith.pays(electric_bill, flatmate2=John))

bill_pdf = PdfReport("Bill_report")

bill_pdf.generate(John,Smith,electric_bill)

