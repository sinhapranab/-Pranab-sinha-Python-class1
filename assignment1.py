students={
    "Pranab":[85,90,88],
    "Rohan":[90,65,89],
    "jeet":[56,78,88],
    "Subham":[95,78,80],
    "Rishi":[89,75,68]
}
def calculate_average(marks):
    return sum(marks)/len(marks)

top_student=""
top_avg=0

def assign_grade(avg):
    if avg>=90:
        return "A"
    elif avg>=75 and avg<89:
        return "B"
    elif avg>=60 and avg<75:
        return "C"
    else:
        return "Fail"

print("Student details: ")

for name,marks in students.items():
    avg = calculate_average(marks)
    grade = assign_grade(avg)
    print(f"Name: {name}, Average: {avg}, Grade: {grade}")

    if avg>top_avg:
        top_avg=avg
        top_student=name

print("Top scorer is: ")
print(f"Name: {top_student}, Average: {top_avg}")

