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

    def pays(self, bill, *args):
        total_days = 0
        for item in args:
            item.days_in_house
            total_days = item.days_in_house + total_days
        weight = self.days_in_house / (total_days)
        to_pay = bill.amount * float(weight)
        return to_pay


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
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='c', ln=1)

        # Insert period label and values
        pdf.cell(w=100, h=40, txt="Period: ", border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        #Insert the name and pay amount for each flatmate
        for flat in args:
            pdf.cell(w=100,h=40,txt=flat.name, border =1)
            pdf.cell(w=150, h=40, txt=str(flat.pays(bill,*args)), border=1, ln=1)

        pdf.output(self.filename + '.pdf')


electric_bill = Bill(120, "March 2020")
John = Flatmate("John", 20)
Smith = Flatmate("Smith", 25)
Jane = Flatmate("Jane",20)

print(John.pays(electric_bill,Smith,John,Jane))
print(Smith.pays(electric_bill,Smith,John,Jane))
print(Jane.pays(electric_bill,Smith,John,Jane))

teddy = John.pays(electric_bill,Smith,John,Jane)+Smith.pays(electric_bill,Smith,John,Jane)+Jane.pays(electric_bill,Smith,John,Jane)

bill_pdf = PdfReport("Bill_report")

bill_pdf.generate(John,Smith,Jane, bill = electric_bill)

