import sys

if len(sys.argv) == 2:
    script_name = sys.argv[0]
    salary = float(sys.argv[1])
    print("User provided input value:")
else:
    script_name = sys.argv[0]
    salary = 30000.0
    print("No input given — using default value:")


bonus = salary * 0.10
total_salary = salary + bonus

print("\n--- Salary Bonus Calculation ---")
print("Script Name:", script_name)
print("Employee Salary:", salary)
print("Bonus Amount (10%):", bonus)
print("Total Salary:", total_salary)
