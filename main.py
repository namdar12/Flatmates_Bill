from flat import Bill, Flatmate
from reports import PdfReport

date = input("Please enter the month: ")
bill_cost = float(input("Please enter the bill cost: "))
number_housemates = int(input("Please enter the number of housemates: "))
bill = Bill(bill_cost, date)

list1 = []
count = 0
while count < number_housemates:
    try:
        Flatmate_p, Flatmate_days = input("Enter Flatmates Name followed by days in house ").split()
        Flatmate_object = Flatmate(Flatmate_p, int(Flatmate_days))
        list1.append(Flatmate_object)
        count += 1
    except:
        print("Please only enter Flatmates Name followed by days in house ")


for user in list1:
    print(user.name)

bill_pdf = PdfReport("Bill Report")
bill_pdf.generate(*list1, bill = bill)
