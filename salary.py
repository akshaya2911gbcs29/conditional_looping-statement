salary=salary=int(input("Enter the salary:"))
leave=int(input("Enter the no of leave:"))
if leave>=0 and leave<=2:
     print("Salary:",salary)
else:
     d=(salary-(leave-2)*500)
     print("Salary:",d)

