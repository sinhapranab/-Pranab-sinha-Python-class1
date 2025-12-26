import student
import attendance
from marks import calculate_total
import fees
from report import Report
from utils import current_date
import moduleInfo

student.add_student(101,"Pranab",22)

attendance.mark_attendance(101,78)

marks=[78,90,89]
total=calculate_total(marks)

fees.pay_fees(101,20000)

report = Report(101,marks)
percentage,grade=report.generate_report()

print("date: ",current_date())
print("student: ",student.get_student(101))
print("attendance: ",attendance.get_attendance(101))
print("total marks: ",total)
print("percentage: ",percentage)
print("grade: ",grade)
print("fees paid: ", fees.get_fees(101))

moduleInfo.show_module_info()
