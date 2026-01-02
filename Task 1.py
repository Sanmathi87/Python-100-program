emp_id = input("Enter Employee ID: ")
emp_name = input("Enter Employee Name: ")
hours_worked = float(input("Enter Total Hours Worked: "))
hourly_rate = float(input("Enter Hourly Rate: "))


if hours_worked <= 40:
    regular_pay = hours_worked * hourly_rate
    overtime_pay = 0
else:
    regular_pay = 40 * hourly_rate
    overtime_hours = hours_worked - 40
    overtime_rate = hourly_rate * 1.5
    overtime_pay = overtime_hours * overtime_rate


total_pay = regular_pay + overtime_pay


print("\n--- Payroll Details ---")
print("Employee ID:", emp_id)
print("Employee Name:", emp_name)
print("Hours Worked:", hours_worked)
print("Hourly Rate:", hourly_rate)
print("Regular Pay:", regular_pay)
print("Overtime Pay:", overtime_pay)
print("Total Pay:", total_pay)
