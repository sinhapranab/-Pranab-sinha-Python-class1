from marks import calculate_percentage,calculate_grade

class Report:
    def __init__(self,roll,marks):
        self.roll = roll
        self.marks = marks

    def generate_report(self):
        percentage=calculate_percentage(self.marks)
        grade=calculate_grade(percentage)
        return percentage,grade
