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