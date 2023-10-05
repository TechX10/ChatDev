'''
This file contains the Budget class which handles income, expense tracking, and reporting.
'''
class Budget:
    def __init__(self):
        self.income = []
        self.expenses = []
    def add_income(self, amount, description):
        # Add income to the list
        self.income.append({"amount": amount, "description": description})
    def add_expense(self, amount, description):
        # Add expense to the list
        self.expenses.append({"amount": amount, "description": description})
    def calculate_total_income(self):
        return sum(income["amount"] for income in self.income)
    def calculate_total_expenses(self):
        return sum(expense["amount"] for expense in self.expenses)
    def generate_report(self):
        # Generate a report with income, expenses, and analytics
        total_income = self.calculate_total_income()
        total_expenses = self.calculate_total_expenses()
        net_income = total_income - total_expenses if total_expenses else total_income
        report = f"Total Income: ${total_income}\n"
        report += f"Total Expenses: ${total_expenses}\n"
        report += f"Net Income: ${net_income}\n"
        return report