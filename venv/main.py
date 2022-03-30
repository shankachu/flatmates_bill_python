class Bill:
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def bills_to_pay(self, bill):
        return bill / self.days_in_house


class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        file_content = self.filename + flatmate1 + flatmate2 + bill
        return file_content


bill1 = Bill(500, 10)
print(bill1.amount)
