class RentalIncome():

    def __init__(self):
        self.total_income = 0
        self.total_expenses = 0
        self.total_cash_flow = 0
        self.total_investment = 0
        self.total_roi = 0

    def income(self):
        print("\nLet's start with income...\n")
        self.rent_income = int(
            input('What is the estimated monthly income from the rental property?'))
        self.storage = int(
            input('What is the estimated montly income from storage?'))
        self.parking = int(
            input('What is the estimated monthly income from parking?'))
        self.misc = int(
            input('What is the estimated monthly income from miscellaneous items?'))

        self.total_income = self.rent_income + self.storage + self.parking + self.misc

        print(f'\nTotal monthly income = {self.total_income}\n')

    def expenses(self):
        print('\nTime to enter expenses...\n')
        self.tax = int(input('What is the monthly tax expense?'))
        self.insurance = int(input('What is the monthly insurance expense?'))
        self.utilities = int(input('What is the monthly utilities expense?'))
        self.hoa = int(input('What is the monthly HOA expense?'))
        self.landscape = int(input('What is the monthly landscaping expense?'))
        self.vacancy = int(input('What is the monthly vacancy expense?'))
        self.repairs = int(input('What is the monthly repair/CapEx expense?'))
        self.manage = int(
            input('What is the monthly property management expense?'))
        self.mortgage = int(input('What is the monthly mortgage expense?'))
        self.misc_ = int(input('What is the monthly miscellaneous expense?'))

        self.total_expenses = self.tax + self.insurance + self.utilities + self.hoa + \
            self.landscape + self.vacancy + self.repairs + \
            self.manage + self.mortgage + self.misc_

        print(f'\nTotal monthly expense = {self.total_expenses}\n')

    def cash_flow(self):
        print('\nCalculating monthly cash flow...\n')

        self.total_cash_flow = self.total_income - self.total_expenses

        print(f'\nTotal monthly cash flow = {self.total_cash_flow}\n')

    def roi(self):
        print("\nLet's wrap things up...\n")
        self.down = int(input('What was the down payment?'))
        self.closing = int(input('What was the closing cost?'))
        self.renivations = int(input('What was the renivating cost?'))
        self.miscellaneous = int(
            input('What was the miscellaneous investing cost?'))

        self.total_investment = self.down + self.closing + \
            self.renivations + self.miscellaneous

        print(f'\nTotal investment = {self.total_investment}\n')

        self.annual_cash_flow = self.total_cash_flow * 12

        self.total_roi = self.annual_cash_flow/self.total_investment * 100

        print(f'\nTotal ROI = {round(self.total_roi,2)}%\n')


total = RentalIncome()


def run():

    while True:

        calculate = input(
            '\nWould you like to calculate the ROI of a rental property? Yes[y] No[n]')

        if calculate.lower() == 'y':
            print(
                '\nFor any value you are not estimating, please enter zero[0]\n\nFor all other values, enter the dollar amount rounded to the nearest dollar amount.\n')

            total.income()
            total.expenses()
            total.cash_flow()
            total.roi()

        elif calculate.lower() == 'n':
            print('\nSee you later!\n')
            break

        else:
            print(
                '\nInvalid respose...\nPlease type "y" for yes OR "n" for no to calculate ROI\n')


run()
